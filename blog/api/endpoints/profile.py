
from django.shortcuts import render
from rest_framework.views import APIView

from .throttling import NoThrottling
from .authentication import MethodAuthentication


class ProfileView(APIView):
    throttle_classes = (NoThrottling, )
    authentication_classes = (MethodAuthentication, )
    permission_classes = ()

    def get(self, request):
        return render(request, 'profile.html')
