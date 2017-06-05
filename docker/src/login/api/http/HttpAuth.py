
class HttpAuth:

    TOKEN = 'ltoken'
    RTOKEN = 't'

    def setTokenCookie(self, response, token):
        response.set_cookie(self.TOKEN, token, domain=self.cookies_domain)

    def getTokenCookie(self, request):
        return request.cookies.get(self.TOKEN)

    def removeTokenCookie(self, response):
        response.set_cookie(self.TOKEN, '', domain=self.cookies_domain, expires=0)
