import logging
from flask import jsonify, url_for, request, abort

from login.api.server import Session
from login.model import LoginModel


def registerApi(app):

    @app.route('/login/api/v1.0/request_redirection_token', methods=['POST'])
    def request_redirection_token():
        """
            obtiene un nuevo token de redirección para una url
            /login/api/v1.0/request_redirection_token
            {
                url: redirection_url
            }
            retorna:
            {
                redirection_token: token
            }
        """
        try:
            url = request.json.get('url')
            rtoken = LoginModel.registerRedirection(url)
            r = {
                'redirection_token': rtoken
            }
            return jsonify(r), 201

        except Exception as e:
            logging.exception(e)
            r = {
                'error': str(e)
            }
            return jsonify(r), 200

    @app.route('/login/api/v1.0/check_token', methods=['POST'])
    def check_token():
        """
            chequea que un token de sesión sea válido
            /login/api/v1.0/check_token
            {
                token: token
            }
            retorna:
            {
                status: True|False
            }
        """
        try:
            token = request.json.get('token')
            LoginModel.checkToken(token)
            r = {
                'status': True
            }
            return jsonify(r), 201

        except Exception as e:
            logging.exception(e)
            r = {
                'satus': False,
                'error': str(e)
            }
            return jsonify(r), 400



    @app.route('/login/api/v1.0/login', methods=['POST'])
    def login():
        try:
            username = request.json.get('username')
            password = request.json.get('password')
            s = Session()
            sid = LoginModel.login(s, username, password)
            return jsonify({'sid':sid}), 201

        except Exception as e:
            logging.exception(e)
            abort(400)
