# coding: utf-8
from __future__ import absolute_import
from blog.celery import app
from django.core.mail import send_mail
from blog.settings import SENDER_MAIL, RECEIVER_MAIL


@app.task
def comment_noti(nickname, article_title):
    send_mail(
        '评论通知',
        '%s 给你的博文 %s 留了言',
        SENDER_MAIL,
        [RECEIVER_MAIL],
        fail_silently=False,
    )
