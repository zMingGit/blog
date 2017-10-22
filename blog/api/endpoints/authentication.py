from django.utils.translation import ugettext_lazy as _

from rest_framework import exceptions
from rest_framework.authentication import SessionAuthentication

from blog.certificate.models import Certificate

class MethodAuthentication():
    def authenticate(self, request):
        if request.method == "GET":
            return None
        else:
            user = getattr(request._request, 'user', None)
            if not user or not user.is_active:
                raise exceptions.AuthenticationFailed('User inactive or deleted.')
            super(MethodAuthentication, self).enforce_csrf(request)
            return (user, None)