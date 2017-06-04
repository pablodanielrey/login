import os
from flask import Flask, request, render_template, make_response, redirect, send_from_directory

from login.api.http import HttpAuthClient

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
httpAuthClient = HttpAuthClient(
                        os.environ['LOGIN_URL'],
                        os.environ['LOGIN_REST_API_URL'])

@app.route('/', methods=['GET'])
@httpAuthClient.require_login
def index():
    app.logger.debug('url requerida : {}'.format(request.url))
    return render_template('protected.html')

@app.route('/<path:path>', methods=['GET'])
@httpAuthClient.require_login
def index_path(path):
    return index()

@app.route('/default_protected', methods=['GET'])
@httpAuthClient.require_login
def default_protected():
    return render_template('default_protected.html')

@app.route('/default', methods=['GET'])
def default():
    return render_template('default.html')

def main():
    app.run(host='0.0.0.0', port=5002, debug=True)

if __name__ == "__main__":
    main()
