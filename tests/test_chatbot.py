""" Unit tests docstring """
import os
import pytest
from app.chatbot import app

@pytest.fixture
def api_client():
    """Defining client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

#pylint: disable=W0621
def test_send_message(api_client, mocker):
    """ Test send message to OpenAI """
    mocker.patch.dict(os.environ, {"OPENAI_API_KEY": "your_fake_api_key"})

    # Mock OpenAI API call
    mock_openai_create = mocker.patch("openai.chat.completions.create")
    mock_openai_create.return_value = {"choices": [{"message": {"content": "Mocked response"}}]}

    # Send a message using the /message endpoint
    response = api_client.post("/message", json={"message": "Test message"})

    assert response.status_code == 200
    assert "response" in response.json
    assert response.json["response"] == "Mocked response"

    # Verify that the OpenAI API was called with the expected arguments
    mock_openai_create.assert_called_once_with(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Test message"},
        ],
    )

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
