# -*- coding: utf-8 -*-
import autobahn

from wamp_utils import WampComponent
from login.model import LoginModel


class Login(WampComponent):

    @autobahn.wamp.register('login.login')
    async def login(self, username, password, details):
        """
            Realiza el login de la persona, retorna un sid en caso de ser correcto y error en caso de error
        """
        return LoginModel.login(username, password)
