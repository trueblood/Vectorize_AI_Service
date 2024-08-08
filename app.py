from flask import Flask, request, jsonify
import tensorflow_hub as hub
import os

app = Flask(__name__)

# Load the Universal Sentence Encoder model
model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Set API Key from Environment Variable
API_KEY = os.getenv('API_KEY', 'your_default_api_key_here')

@app.route('/vectorize', methods=['POST'])
def vectorize():
    # Check for API Key in the request header
    if request.headers.get('X-API-KEY') != API_KEY:
        return jsonify({'error': 'Unauthorized access'}), 401

    data = request.get_json()
    sentence = data.get('sentence')
    request_id = data.get('id')  # Retrieve the ID from the request

    if not sentence:
        return jsonify({'error': 'No sentence provided'}), 400
    if not request_id:
        return jsonify({'error': 'No ID provided'}), 400

    # Generate vector
    vector = model([sentence])[0].numpy()
    vector = vector.tolist()  # Convert numpy array to list for JSON serialization

    return jsonify({'id': request_id, 'vector': vector})

# Health check method
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    # Dynamically bind to the port provided by Cloud Run
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
