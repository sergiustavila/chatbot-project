""" Unit tests docstring """
from fastapi.testclient import TestClient
from app.chatbot import app

client = TestClient(app)


def test_health_root():
    """Function docstring"""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {'status': 'Chatbot is healthy'}


def test_version_root():
    """Function docstring"""
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}
