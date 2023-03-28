# app/routes/main.py

from flask import jsonify
from sqlalchemy import inspect, text
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


@main_blueprint.route('/api/v1/tables/<table_name>', methods=['GET'])
def get_table_data(table_name):
    # Validate if the table exists
    inspector = inspect(db.engine)
    if table_name not in inspector.get_table_names():
        return jsonify({'error': f"Table '{table_name}' not found"}), 404

    # Fetch all the data from the table
    try:
        result = db.engine.execute(text(f"SELECT * FROM {table_name}"))
        column_names = result.keys()
        data = [dict(zip(column_names, row)) for row in result]

        return jsonify(data)
    except Exception as err:
        return jsonify({'error': str(err)}), 500
