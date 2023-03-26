import os

from flask import Flask
from flask_socketio import SocketIO

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


# TODO: Remove CORS in production
CORS(app)  # This will enable CORS for all routes

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'sqlite_db/my_database.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from . import routes
