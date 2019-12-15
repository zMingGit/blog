from rest_framework import exceptions
from rest_framework.authentication import SessionAuthentication


class MethodAuthentication(SessionAuthentication):
    def authenticate(self, request):
        if request.method == "GET":
            return None
        else:
            return None
            user = getattr(request._request, 'user', None)
            if not user or not user.is_active:
                raise exceptions.AuthenticationFailed('User inactive or deleted.')
            super(MethodAuthentication, self).enforce_csrf(request)
            return (user, None)
