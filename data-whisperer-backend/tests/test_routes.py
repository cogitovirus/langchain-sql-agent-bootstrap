# tests/test_routes.py

import json

def test_get_tables(client):
    response = client.get('/api/v1/tables')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_table_data(client):
    # Use a table name that exists in your test database
    table_name = 'customers'
    response = client.get(f'/api/v1/tables/{table_name}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_get_table_data_not_found(client):
    # Use a table name that does not exist in your test database
    table_name = 'non_existent_table'
    response = client.get(f'/api/v1/tables/{table_name}')
    assert response.status_code == 404