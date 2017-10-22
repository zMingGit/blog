import re
from django.shortcuts import render_to_response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .throttling import NoThrottling
from .authentication import MethodAuthentication
from blog.article.models import Article


class ArticleView(APIView):
    throttle_classes = (NoThrottling, )
    authentication_classes = (MethodAuthentication, )
    permission_classes = ()

    def get(self, request):
        op = request.GET.get('type', None)
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
        article_types = Article.objects.get_all_article_type()
        re_html = re.compile('<.*?>')
        data.title = re_html.sub('', data.title)
        return render_to_response('article.html', {
            'article_types': article_types,
            'title': 'Z-M | ' + data.title,
            'context': data.context
        })

    def post(self, request):
        return Response({'post': 'make sure has been input the password'})
