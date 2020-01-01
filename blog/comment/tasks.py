# coding: utf-8
from __future__ import absolute_import
from blog.celery import app
from django.core.mail import send_mail


@app.task
def comment_noti(nickname, article_title):
    send_mail(
        '评论通知',
        '%s 给你的博文 %s 留了言',
        'email@zming.info',
        ['email@zming.info'],
        fail_silently=False,
    )
