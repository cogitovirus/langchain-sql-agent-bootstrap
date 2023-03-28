# tests/conftest.py

import pytest
from app import create_app
from tests.Config import Config

@pytest.fixture
def app():
    print("Test database URI:", Config.SQLALCHEMY_DATABASE_URI)  # Add this line to print the database URI

    app = create_app(Config)
    return app

@pytest.fixture
def client(app):
    return app.test_client()
