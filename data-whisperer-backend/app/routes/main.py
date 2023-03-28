# app/routes/main.py

from flask import jsonify
from sqlalchemy import inspect
from ..models import db
from . import main_blueprint

@main_blueprint.route('/api/v1/tables', methods=['GET'])
def get_tables():
    """
    Get a list of all tables in the database
    """
    inspector = inspect(db.engine)
    table_names = inspector.get_table_names()
    return jsonify(table_names)
