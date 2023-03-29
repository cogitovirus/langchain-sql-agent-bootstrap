# app/config.py

import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'sqlite_db/my_database.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = f"sqlite:///{os.path.join(basedir, 'uploads')}"
    MODEL_NAME = os.environ.get('MODEL_NAME')
