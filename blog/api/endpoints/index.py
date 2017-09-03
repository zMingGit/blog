import markdown

from django.shortcuts import render_to_response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from .throttling import NoThrottling
from .authentication import MethodAuthentication
from blog.article.models import Article


class IndexView(APIView):
    throttling_classes = (NoThrottling, )
    authentication_classes = (MethodAuthentication, )
    permission_classes = ()

    def get(self, request):
        return render_to_response('index.html')
