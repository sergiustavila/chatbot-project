""" Module docstring """
import os
from flask import Flask, jsonify, request
import openai

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/message", methods=["POST"])
def send_message():
    """Message endpoint"""
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"error": "Invalid request"})

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ],
    )

    return jsonify({"response": response["choices"][0]["message"]["content"]})

@app.route("/healthcheck")
def healthcheck():
    """Healthcheck endpoint"""
    return jsonify({"status": "Chatbot is healthy"})

@app.route("/version")
def get_version():
    """Version endpoint"""
    with open("VERSION", "r", encoding='utf-8') as file:
        version = file.read().strip()
        return jsonify({"version": version})


if __name__ == "__main__":
    app.run(debug=True)
