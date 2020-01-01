# coding: utf-8
from django.shortcuts import render
from rest_framework.views import APIView

from .throttling import NoThrottling
from .authentication import MethodAuthentication

from blog.item.models import ReaderItem
from blog.api.endpoints.common import get_remote_ip_and_ua


class ProfileView(APIView):
    throttle_classes = (NoThrottling, )
    authentication_classes = (MethodAuthentication, )
    permission_classes = ()

    def get(self, request):
        ip, ua = get_remote_ip_and_ua(request)
        item = ReaderItem.objects.get_one(ip)
        if item:
            ReaderItem.objects.read_item(item, ip, ua)
        return render(request, 'profile.html', {
            'item': item
        })
