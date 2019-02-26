import uuid
from django.utils.deprecation import MiddlewareMixin

USER_KEY = 'uid'
TEN_YEARS = 60 * 60 * 60 * 365 * 10


class UserIDMiddleware(MiddlewareMixin):

    def __call__(self, request):
        uid = self.generate_uid(request)
        request.uid = uid
        response = self.get_response(request)
        response.set_cookie(USER_KEY, uid, max_age=TEN_YEARS, httponly=True)

    def generate_uid(self, request):
        try:
            uid = request.COOKIES[USER_KEY]
        except KeyError:
            uid = uuid.uuid4().hex

        return uid
