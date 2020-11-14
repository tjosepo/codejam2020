import functools

from flask import Blueprint
from flask.helpers import send_file
from flask.json import jsonify
from api.db import get_db

bp = Blueprint('api', __name__)


@bp.route('/cdn/<string:filename>', methods=['GET'])
def static(filename):
    return send_file(f'cdn/{filename}', mimetype='image/jpg')


@bp.route('/query/<string:type>', methods=['GET'])
def query_type(type):
    db = get_db()
    images = None
    if (type == 'shirt'):
        images = db.execute('SELECT * FROM image WHERE shirt = 1').fetchall()
    if (type == 'top'):
        images = db.execute('SELECT * FROM image WHERE top = 1').fetchall()
    if (type == 'sweater'):
        images = db.execute('SELECT * FROM image WHERE sweater = 1').fetchall()
    if (type == 'cardigan'):
        images = db.execute(
            'SELECT * FROM image WHERE cardigan = 1').fetchall()
    if (type == 'jacket'):
        images = db.execute('SELECT * FROM image WHERE jacket = 1').fetchall()
    if (type == 'vest'):
        images = db.execute('SELECT * FROM image WHERE vest = 1').fetchall()
    if (type == 'pants'):
        images = db.execute('SELECT * FROM image WHERE pants = 1').fetchall()
    if (type == 'shorts'):
        images = db.execute('SELECT * FROM image WHERE shorts = 1').fetchall()
    if (type == 'skirt'):
        images = db.execute('SELECT * FROM image WHERE skirt = 1').fetchall()
    if (type == 'coat'):
        images = db.execute('SELECT * FROM image WHERE coat = 1').fetchall()
    if (type == 'dress'):
        images = db.execute('SELECT * FROM image WHERE dress = 1').fetchall()
    if (type == 'jumpsuit'):
        images = db.execute(
            'SELECT * FROM image WHERE jumpsuit = 1').fetchall()
    if (type == 'cape'):
        images = db.execute('SELECT * FROM image WHERE cape = 1').fetchall()
    if (type == 'glasses'):
        images = db.execute('SELECT * FROM image WHERE glasses = 1').fetchall()
    if (type == 'hat'):
        images = db.execute('SELECT * FROM image WHERE hat = 1').fetchall()
    if (type == 'headband'):
        images = db.execute(
            'SELECT * FROM image WHERE headband = 1').fetchall()
    if (type == 'tie'):
        images = db.execute('SELECT * FROM image WHERE tie = 1').fetchall()
    if (type == 'glove'):
        images = db.execute('SELECT * FROM image WHERE glove = 1').fetchall()
    if (type == 'watch'):
        images = db.execute('SELECT * FROM image WHERE watch = 1').fetchall()
    if (type == 'belt'):
        images = db.execute('SELECT * FROM image WHERE belt = 1').fetchall()
    if (type == 'sock'):
        images = db.execute('SELECT * FROM image WHERE sock = 1').fetchall()
    if (type == 'shoe'):
        images = db.execute('SELECT * FROM image WHERE shoe = 1').fetchall()
    if (type == 'bag'):
        images = db.execute('SELECT * FROM image WHERE bag = 1').fetchall()
    if (type == 'scarf'):
        images = db.execute('SELECT * FROM image WHERE scarf = 1').fetchall()
    if (type == 'hood'):
        images = db.execute('SELECT * FROM image WHERE hood = 1').fetchall()
    if images is None:
        return jsonify([])

    json = []
    for image in images:
        image_json = {
            'id': image['id'],
            'file': image['file'],
        }
        json.append(image_json)
    return jsonify(json)


def init_app(app):
    app.register_blueprint(bp)
