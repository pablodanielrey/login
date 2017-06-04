import logging
from flask import jsonify, url_for, request, abort

from login.model import LoginModel


def registerApi(app):

    @app.route('/login/api/v1.0/login', methods=['POST'])
    def login():
        username = request.json.get('username')
        password = request.json.get('password')
        try:
            sid = LoginModel.login(username, password)
            return jsonify({'sid':sid}), 201

        except Exception as e:
            logging.exception(e)
            abort(400)
