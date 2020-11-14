from os import path
from api.db import get_db
import json
import requests
import io
import base64
import pandas as pd
from PIL import Image

import click
import os

from flask import current_app, g
from flask.cli import with_appcontext
from . import db
import shutil


class ImageByteEncoder:
    """Class that provides functionalities to encode an image to bytes and
    decode back to image
    """

    def encode(self, img):
        """Encode

        Arguments:
            img {Image} -- PIL Image to be encode

        Returns:
            str -- image encoded as a string
        """
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()
        img_bytes = base64.b64encode(img_bytes).decode('utf8')
        return img_bytes

    def decode(self, img_str):
        """Decode

        Arguments:
            img_str {str} -- Image str as encoded by self.encode

        Returns:
            Image -- PIL Image
        """
        img_bytes = bytes(img_str, encoding='utf8')
        img_bytes = base64.b64decode(img_bytes)
        img = Image.open(io.BytesIO(img_bytes))
        return img


class Segmenter:
    def __init__(self):
        self.inference_url = 'https://models.samasource.com/fashion-seg/invocations'
        self.encoder = ImageByteEncoder()

    def _predict(self, req_json):
        # Request
        response = requests.post(
            url=self.inference_url,
            data=req_json,
            headers={"Content-Type": "application/json"})
        response = json.loads(response.text)[0]

        # Decode the seg info
        seg_str = response['Mask']
        id_to_class = json.loads(response['Mapping'])
        seg = self.encoder.decode(seg_str)
        return seg, id_to_class

    def predict_on_image(self, img):
        # Encode image as Byte String
        img_str = self.encoder.encode(img)

        # Create json request for the service according to pandas schema
        req_df = pd.DataFrame({'Image': [img_str]})
        req_json = req_df.to_json(orient='split')
        return self._predict(req_json)

    def predict_on_url(self, url):
        # Create json request for the service according to pandas schema
        req_df = pd.DataFrame({'Image_url': [url]})
        req_json = req_df.to_json(orient='split')
        return self._predict(req_json)


def get_image_from_url(img_url):
    response = requests.get(img_url)
    img = Image.open(io.BytesIO(response.content))
    return img


def get_image_from_path(filename):
    img = Image.open(filename, mode='r')
    return img


def classify_images():
    segmenter = Segmenter()
    db = get_db()
    img_dir = "./images/"
    files = os.listdir(img_dir)
    for file in files:
        # Check if file is in cdn
        if path.exists(f'./api/cdn/{file}') is False:
            shutil.copy(f'./images/{file}', f'./api/cdn/{file}')

        # Check if image is already in db
        if db.execute('SELECT id FROM image WHERE file = ?', (file,)).fetchone() is not None:
            continue

        # Classify file
        click.echo(f'Classifying {file}...')
        img = get_image_from_path(img_dir + file)
        _, id_to_class = segmenter.predict_on_image(img)

        # Add image to db
        db.execute(
            'INSERT INTO image (file, shirt, top, sweater, cardigan, jacket, vest, pants, shorts, skirt, coat, dress, jumpsuit, cape, glasses, hat, headband, tie, glove, watch, belt, sock, shoe, bag, scarf, hood) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (file, '1' in id_to_class, '2' in id_to_class, '3' in id_to_class, '4' in id_to_class, '5' in id_to_class, '6' in id_to_class, '7' in id_to_class, '8' in id_to_class, '9' in id_to_class, '10' in id_to_class, '11' in id_to_class,
             '12' in id_to_class, '13' in id_to_class, '14' in id_to_class, '15' in id_to_class, '16' in id_to_class, '17' in id_to_class, '18' in id_to_class, '19' in id_to_class,  '20' in id_to_class,  '23' in id_to_class,
             '24' in id_to_class,  '25' in id_to_class, '26' in id_to_class,  '28' in id_to_class)
        )
        db.commit()


@click.command('classify-images')
@with_appcontext
def classify_images_command():
    """Adds images from the images/ folder to the database"""
    classify_images()
    click.echo('Classified images.')


def init_app(app):
    app.cli.add_command(classify_images_command)
