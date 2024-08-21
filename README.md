# Vectorize_AI_Service
API for hosting https://tfhub.dev/google/universal-sentence-encoder/4 and transforming strings into vectors

# Sentence Vectorization API

This repository hosts a Flask-based API that leverages the sentence-transformers library to convert sentences into 384-dimensional vectors. This vectorization process is essential for natural language processing applications that require sentence embedding for tasks such as semantic search, clustering, and text similarity.

## Getting Started

### Prerequisites

- Python 3.7 or higher.
- An API key stored as an environment variable for authentication purposes.

### Installation

Clone this repository to your local machine:
   ```bash
    git clone https://github.com/trueblood/Vectorize_AI_Service.git
    cd sentence-vectorization-api
    pip install -r requirements.txt
    cd sentence-vectorization-api
    pip install -r requirements.txt
    python app.py
    ```

### API Endpoints

POST /vectorize: Vectorizes a given sentence into a 384-length vector.
Requires a JSON payload with a sentence and an id.
Requires an API key passed in the header under X-API-KEY.
GET /health: Returns the health status of the API, useful for uptime monitoring and health checks.




