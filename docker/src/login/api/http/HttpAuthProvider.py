"""
    Este código es usado por el provider de autentificación, por lo que es seguro acceder al modelo
"""
from functools import wraps
from flask import request, make_response, redirect, render_template

from login.model import LoginModel
from login.api.http.HttpAuth import HttpAuth

class HttpAuthProvider(HttpAuth):

    def __init__(self, default_site, cookies_domain):
        super().__init__()
        self.default_site = default_site
        self.cookies_domain = cookies_domain

    """
        algunos exploradores no setean las cookies cuando se realiza una redireccion usando 302
    def redirect_to_site(self, req):
        try:
            rtoken = req.args.get(self.RTOKEN)
            url = LoginModel.checkRedirectionToken(rtoken)
            return make_response(redirect(url, code=302))

        except Exception as e:
            return make_response(redirect(self.default_site, code=302))
    """

    def redirect_with_template(self, url):
        return make_response(render_template('redirect.html', url=url))

    def redirect_to_site_with_template(self, red):
        """ redirecciona al sitio correcto definido por el redirection_token registrado por un cliente usando la api rest (HttpAuthClient.require_login) """
        try:
            rtoken = req.args.get(self.RTOKEN)
            url = LoginModel.checkRedirectionToken(rtoken)
            return self.redirect_with_template(url)

        except Exception as e:
            return self.redirect_with_template(self.default_site)


    def redirect_on_token(self, f):
        """ chequea el token de autentificación y si existe redirecciona al sitio correcto registrado """
        @wraps(f)
        def decorated(*args, **kwargs):
            try:
                token = self.getTokenCookie(request)
                LoginModel.checkToken(token)
                return self.redirect_to_site_with_template(request)

            except Exception as e:
                return f(*args, **kwargs)
        return decorated
