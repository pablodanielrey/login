from flask import Flask, request, send_from_directory

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/src/login/web')

@app.route('/<path:path>')
def send(path):
    return send_from_directory(app.static_url_path, path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
