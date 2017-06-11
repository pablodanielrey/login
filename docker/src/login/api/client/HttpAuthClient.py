import requests
from functools import wraps
from flask import request, make_response, redirect

from login import InvalidTokenException
from login.api import HttpAuth

class HttpAuthClient(HttpAuth):

    def __init__(self, login_url, rest_api_url):
        super().__init__()
        self.login_url = login_url
        self.rest_api_url = rest_api_url

    def _getRedirectionToken(self, url):
        """ obtiene un token de redirección para una determinada url """
        req_url = '{}{}'.format(self.rest_api_url, '/login/api/v1.0/request_redirection_token')
        req_data = {
            'url': url
        }
        resp = requests.post(req_url, json=req_data)
        return resp.json().get('redirection_token')

    def _checkToken(self, token):
        """ chequea que el token de sesión sea válido """
        req_url = '{}{}'.format(self.rest_api_url, '/login/api/v1.0/check_token')
        req_data = {
            'token': token
        }
        resp = requests.post(req_url, json=req_data)
        if not resp.json().get('status'):
            raise InvalidTokenException()
        return


    def require_login(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            try:
                token = self.getTokenCookie(request)
                self._checkToken(token)
                return f(*args, **kwargs)

            except Exception as e:
                rtoken = self._getRedirectionToken(request.url)
                if not rtoken:
                    response = make_response("No se pudo obtener el token de redirect", code=401)
                    return response
                url = '{}?{}={}'.format(self.login_url, self.RTOKEN, rtoken)
                response = make_response(redirect(url, code=302))
                return response

        return decorated
