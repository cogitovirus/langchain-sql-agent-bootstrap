# app/routes/upload_file.py

import os
from werkzeug.utils import secure_filename
from flask import request, jsonify, current_app

from . import main_blueprint
from ..services import create_and_load_table

ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main_blueprint.route('/api/v1/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            database = 'path/to/your/sqlite/db.sqlite'
            table_name = 'your_table_name'

            create_and_load_table(file_path, database, table_name)
            return jsonify({'message': 'File uploaded and processed successfully'}), 200
    return jsonify({'error': 'Invalid request'}), 400

