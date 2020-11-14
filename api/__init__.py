import os

from flask import Flask
from flask_cors import CORS
from . import db
from . import sama
from . import api


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, static_folder='/static',
                instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
    )
    CORS(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    sama.init_app(app)
    api.init_app(app)

    return app
