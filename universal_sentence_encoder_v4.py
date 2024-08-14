from flask import Flask, request, jsonify
import tensorflow_hub as hub
import numpy as np

app = Flask(__name__)

# Load the Universal Sentence Encoder model
model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

@app.route('/vectorize', methods=['POST'])
def vectorize():
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
