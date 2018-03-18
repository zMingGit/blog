import re
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .throttling import NoThrottling
from .authentication import MethodAuthentication
from blog.article.models import Article
from blog.comment.models import Comment


class ArticleView(APIView):
    throttle_classes = (NoThrottling, )
    authentication_classes = (MethodAuthentication, )
    permission_classes = ()

    def get(self, request):
        op = request.GET.get('type', None)
        cmt_page = request.GET.get('cmt_page', 1)
        if not isinstance(cmt_page, int):
            return Response('comment page invalid.', status.HTTP_400_BAD_REQUEST)
        if cmt_page < 1:
            cmt_page = 1
        if op is None or op not in ['uuid', 'title']:
            return Response('invalid type', status.HTTP_400_BAD_REQUEST)

        if op == 'uuid':
            uuid = request.GET.get('uuid', None)
            if uuid is None:
                return Response('uuid can not be empty',
                                status.HTTP_400_BAD_REQUEST)
            data = Article.objects.get_article_by_id(uuid)
        elif op == 'title':
            title = request.GET.get('title', None)
            if title is None:
                return Response('title can not be empty',
                                status.HTTP_400_BAD_REQUEST)
            data = Article.objects.get_article_by_title(title)
        if data is None:
            return Response("can't found this article")
        re_html = re.compile('<.*?>')
        data.title = re_html.sub('', data.title)
        

        comments = Comment.objects.get_comment_by_page(data.uuid, cmt_page)
        return render(request, 'article.html', {
            'title': data.title,
            'context': data.context,
            'comments': comments
        })

    def post(self, request):
        return Response({'post': 'make sure has been input the password'})
