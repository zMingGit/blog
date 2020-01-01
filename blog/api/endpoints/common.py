# coding: utf-8
from __future__ import absolute_import


def get_remote_ip_and_ua(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', '-')
    ua = request.META['HTTP_USER_AGENT']
    return ip, ua
