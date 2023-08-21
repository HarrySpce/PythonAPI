from flask import Flask, request, jsonify
from flask_cors import CORS
from data import entries

app = Flask(__name__)
CORS(app)

API_KEY = "hezen"

def is_valid_api_key(api_key):
    return api_key == API_KEY

@app.route('/api/entries', methods=['GET'])
def get_all_entries():
    api_key = request.headers.get('X-API-Key')

    if not api_key or not is_valid_api_key(api_key):
        return jsonify({'error': 'Unauthorized, please check API key.'}), 401

    return jsonify(entries)

if __name__ == '__main__':
    app.run()
