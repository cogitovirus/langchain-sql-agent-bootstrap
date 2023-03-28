# app/__init__.py

from flask import Flask
from flask_cors import CORS
from .models import db, ma
from .routes import main_blueprint

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # TODO: CORS should be restricted to only the frontend domain on production
    # This will enable CORS for all routes
    CORS(app)

    # database init

    db.init_app(app)
    ma.init_app(app)


    app.register_blueprint(main_blueprint)

    return app
