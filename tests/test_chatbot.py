""" Unit tests docstring """
import pytest
from app.chatbot import app

@pytest.fixture
def api_client():
    """Defining client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

#pylint: disable=W0621
def test_health_root(api_client):
    """Function docstring"""
    response = api_client.get("/healthcheck")

    assert response.status_code == 200
    assert response.json == {'status': 'Chatbot is healthy'}

#pylint: disable=W0621
def test_version_root(api_client):
    """Function docstring"""
    response = api_client.get("/version")

    assert response.status_code == 200
    assert response.json == {"version": "1.0.0"}
