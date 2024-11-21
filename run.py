from app import app
import os

@app.route('/')
def root():
    return {'status': 'ok'}, 200

@app.route('/health')
def health_check():
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
