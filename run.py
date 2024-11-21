from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return {'status': 'ok'}, 200

@app.route('/health')
def health():
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))
