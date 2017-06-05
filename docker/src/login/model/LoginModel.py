import os
import uuid
import logging
logging.getLogger().setLevel(logging.DEBUG)
import redis
from itsdangerous import URLSafeSerializer

from login import InvalidTokenException

class LoginModel:

    KEY = '32r09f0f929nr23rfm3249r84jc3'
    SERIALIZER = URLSafeSerializer(KEY)
    REDIS = redis.StrictRedis(
                    host=os.environ['LOGIN_REDIS_HOST'],
                    port=os.environ['LOGIN_REDIS_PORT'],
                    db=os.environ['LOGIN_REDIS_DB'])

    @classmethod
    def login(cls, username, password):
        token = cls.SERIALIZER.dumps(username + cls.KEY)
        cls.REDIS.set(token, username)
        return token

    @classmethod
    def logout(cls, token):
        cls.REDIS.delete(token)

    @classmethod
    def checkToken(cls, token):
        logging.debug('checkToken : {}'.format(token))
        if not token:
            raise InvalidTokenException()
        user = cls.REDIS.get(token)
        if not user:
            raise InvalidTokenException
        return True

    @classmethod
    def registerRedirection(cls, url):
        logging.debug('registerRedirection : {}'.format(url))
        token = cls.SERIALIZER.dumps(str(uuid.uuid4()))
        cls.REDIS.set(token, url, ex='60')
        logging.debug('registerRedirection token {}'.format(token))
        return token

    @classmethod
    def checkRedirectionToken(cls, token):
        logging.debug('checkRedirectionToken : {}'.format(token))
        if not token:
            raise InvalidTokenException()
        url = cls.REDIS.get(token)
        if not url:
            raise InvalidTokenException()
        #cls.REDIS.delete(token)
        logging.debug('checkRedirectionToken url : {}'.format(url))
        return url
