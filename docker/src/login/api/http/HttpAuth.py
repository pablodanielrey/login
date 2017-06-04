
class HttpAuth:

    TOKEN = 'ltoken'
    RTOKEN = 't'

    def setTokenCookie(self, response, token):
        response.set_cookie(self.TOKEN, token)

    def getTokenCookie(self, request):
        return request.cookies.get(self.TOKEN)

    def removeTokenCookie(self, response):
        response.set_cookie(self.TOKEN, '', expires=0)
