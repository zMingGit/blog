import logging

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from .endpoints.throttling import NoThrottling


class Ping(APIView):
    throttle_classes = (NoThrottling, )
    permission_classes = ()

    def get(self, request):
        return Response('Pong')

    def head(self, request):
        return Response(headers={'foo': 'bar',})
