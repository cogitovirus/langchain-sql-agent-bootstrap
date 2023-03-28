# tests/test_upload.py

import os
import io
import json
from app import db
from flask import current_app
from werkzeug.datastructures import FileStorage

def test_upload_file(client, app):
    # Create an in-memory file with some content
    file_content = b"column1,column2\nvalue1,value2"
    file_storage = FileStorage(stream=io.BytesIO(file_content), filename="test.csv", content_type="text/csv")

    response = client.post('/api/v1/upload', content_type='multipart/form-data', data={'file': file_storage})

    assert response.status_code == 200
    assert json.loads(response.data) == {'message': 'File uploaded and processed successfully'}

    # Check if the file was uploaded to the UPLOAD_FOLDER
    uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], "test.csv")
    assert os.path.exists(uploaded_file_path)

    # Clean up the uploaded file after testing
    os.remove(uploaded_file_path)

    # Check if the table was created in the database
    table_name = "test"
    with app.app_context():
        result = db.engine.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        assert result.fetchone()[0] == table_name

        # Check if the data was inserted into the table
        result = db.engine.execute(f"SELECT * FROM {table_name}")
        assert result.fetchone() == ('value1', 'value2')
