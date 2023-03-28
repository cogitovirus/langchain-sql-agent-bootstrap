# app/routes/upload_file.py

import os
from werkzeug.utils import secure_filename
from flask import request, jsonify, current_app

from . import main_blueprint
from ..services import create_and_load_table
from ..models import db


ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main_blueprint.route('/api/v1/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        # Split the filename into name and extension and use the name as the table_name
        table_name, _ = os.path.splitext(filename)

        create_and_load_table(file_path, db, table_name)
        return jsonify({'message': 'File uploaded and processed successfully'}), 200
    return jsonify({'error': 'Invalid request'}), 400
