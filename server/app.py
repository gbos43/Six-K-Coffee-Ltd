from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='../build', static_url_path='/')

@app.route('/api/hello')
def hello_api():
    return jsonify(message="Hello from Flask API!")

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)