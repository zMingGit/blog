import re
import datetime
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .throttling import NoThrottling
from .authentication import MethodAuthentication
from blog.api.endpoints.common import get_remote_ip_and_ua
from blog.article.models import Article, ArticleStatsRecord
from blog.comment.models import Comment
from blog.comment.views import add_comment


class ArticleView(APIView):
    throttle_classes = (NoThrottling, )
    authentication_classes = (MethodAuthentication, )
    permission_classes = ()

    def get(self, request):
        ip, ua = get_remote_ip_and_ua(request)
        op = request.GET.get('type', None)
        cmt_page = request.GET.get('cmt_page', 1)
        if not isinstance(cmt_page, int):
            return Response('comment page invalid.', status.HTTP_400_BAD_REQUEST)
        if cmt_page < 1:
            cmt_page = 1
        if op not in ['uuid', 'title', None]:
            return Response('invalid type', status.HTTP_400_BAD_REQUEST)

        if op == 'uuid' or op is None:
            uuid = request.GET.get('uuid', None)
            if uuid is None:
                return Response('uuid can not be empty',
                                status.HTTP_400_BAD_REQUEST)
            article = Article.objects.get_article_by_id(uuid)
        elif op == 'title':
            title = request.GET.get('title', None)
            if title is None:
                return Response('title can not be empty',
                                status.HTTP_400_BAD_REQUEST)
            article = Article.objects.get_article_by_title(title)

        if article is None:
            return Response("can't found this article")
        re_html = re.compile('<.*?>')
        article.title = re_html.sub('', article.title)
        uuid = article.uuid

        comments = Comment.objects.get_comment_by_page(article.uuid, cmt_page)
        ArticleStatsRecord.objects.create_visit_record(article, ip, ua)
        return render(request, 'article.html', {
            'title': article.title,
            'context': article.context,
            'comments': comments,
            'uuid': uuid,
            'ctime': article.create_time,
            'image': article.image
        })

    def post(self, request):
        return Response({'post': 'make sure has been input the password'})


class CommentView(APIView):
    throttle_classes = (NoThrottling, )
    authentication_classes = (MethodAuthentication, )
    permission_classes = ()

    def put(self, request):
        article = request.data.get('article', None)
        comment = request.data.get('comment', None)
        email = request.data.get('email', '')
        nickname = request.data.get('nickname', None)
        if not comment or not nickname:
            return Response('invalid type', status.HTTP_400_BAD_REQUEST)
        ip, ua = get_remote_ip_and_ua(request)
        dt = datetime.datetime.now()
        add_comment(article, ip, ua, dt, nickname, comment, email)
        return Response({'success': True})
