# app/routes/__init__.py

from flask import Blueprint

main_blueprint = Blueprint('main', __name__)

from . import main, run_command, upload_file
