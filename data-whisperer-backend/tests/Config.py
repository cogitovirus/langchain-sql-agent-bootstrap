# tests/Config.py

import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'sqlite_db/test_database.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
