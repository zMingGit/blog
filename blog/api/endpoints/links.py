# coding: utf-8
from django.shortcuts import render
from rest_framework.views import APIView

from .throttling import NoThrottling
from blog.link.models import Link
from .authentication import MethodAuthentication


class LinksView(APIView):
    throttle_classes = (NoThrottling, )
    authentication_classes = (MethodAuthentication, )
    permission_classes = ()

    def get(self, request):
        links = Link.objects.get_all()
        return render(request, 'links.html', {
            'links': links
        })
