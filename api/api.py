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
    images = db.execute(f'SELECT * FROM image WHERE {type} > 0 ORDER BY {type} DESC').fetchall()
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

@bp.route('/inc/<string:img_id>/<string:type>', methods=['GET'])
def inc_image(img_id, type):
    db = get_db()
    image = db.execute('SELECT * FROM image WHERE id = (?)', (img_id,)).fetchone()
    db.execute(f'UPDATE image SET {type} = (?) WHERE id = (?)', ( int(image[type] + 1), img_id,))
    db.commit()
    return ''

def init_app(app):
    app.register_blueprint(bp)
