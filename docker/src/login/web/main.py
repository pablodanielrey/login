import os
from functools import wraps
from flask import Flask, request, render_template, make_response, redirect, send_from_directory
from login.api.http import HttpAuthProvider
from login.model import LoginModel

# set the project root directory as the static folder, you can set others.
#app = Flask(__name__, static_url_path='/src/login/web/angular')
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
httpAuthProvider = HttpAuthProvider(
                        os.environ['LOGIN_DEFAULT_SITE'],
                        os.environ['LOGIN_COOKIES_DOMAIN'])

@app.route('/favicon.ico', methods=['GET','POST'])
def favicon():
    return send_from_directory(app.static_url_path, 'favicon.ico')

@app.route('/logout', methods=['GET','POST'])
def logout():
    token = httpAuthProvider.getTokenCookie(request)
    LoginModel.logout(token)
    resp = httpAuthProvider.redirect_with_template('/')
    httpAuthProvider.removeTokenCookie(resp)
    return resp

@app.route('/logout/<path:path>', methods=['GET','POST'])
def logout_path(path):
    logout()


@app.route('/', methods=['GET'])
@httpAuthProvider.redirect_on_token
def index():
    return render_template('login.html')

@app.route('/<path:path>', methods=['GET'])
@httpAuthProvider.redirect_on_token
def index_path(path):
    return index()


@app.route('/', methods=['POST'])
@httpAuthProvider.redirect_on_token
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        return index()
    app.logger.info('testeando usuario y clave')
    token = LoginModel.login(username, password)
    app.logger.info('token auth generado : {}'.format(token))
    response = httpAuthProvider.redirect_to_site_with_template(request)
    httpAuthProvider.setTokenCookie(response, token)
    return response

@app.route('/<path:path>', methods=['POST'])
@httpAuthProvider.redirect_on_token
def login_path(path):
    return login()

"""
esto es para el estilo de angular
@app.route('/<path:path>')
def send(path):
    return send_from_directory(app.static_url_path, path)
"""

def main():
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    main()
