from flask import Flask, jsonify, request
import openai

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = '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'

# /message endpoint
@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    message = data.get('message')

    if not message:
        return jsonify({'error': 'Invalid request'})

    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )

    return jsonify({'response': response['choices'][0]['message']['content']})

# /healthcheck endpoint
@app.route('/healthcheck')
def healthcheck():
    return jsonify({'status': 'Chatbot is healthy'})

# /version endpoint
@app.route('/version')
def version():
    with open('VERSION', 'r') as file:
        version = file.read().strip()
        return jsonify({'version': version})

if __name__ == '__main__':
    app.run(debug=True)
