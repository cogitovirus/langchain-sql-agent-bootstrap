# tests/test_routes.py

import json

def test_get_tables(client):
    response = client.get('/api/v1/tables')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)