import markdown

from django.shortcuts import render_to_response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from .throttling import NoThrottling
from .authentication import MethodAuthentication
from blog.article.models import Article


class ArticleView(APIView):
    throttle_classes = (NoThrottling, )
    authentication_classes = (MethodAuthentication, )
    permission_classes = ()

    def get(self, request):
        op = request.GET.get('op', None)
        if op is None or op not in ['uuid', 'title']:
            return Response('invalid type', status.HTTP_400_BAD_REQUEST)

        if op == 'uuid':
            uuid = request.GET.get('uuid', None)
            if uuid is None:
                return Response('uuid can not be empty', status.HTTP_400_BAD_REQUEST)
            data = Article.objects.get_article_by_id(uuid)
        elif op == 'title':
            title = request.GET.get('title', None)
            if title is None:
                return Response('title can not be empty', status.HTTP_400_BAD_REQUEST)
            data = Article.objects.get_article_by_title(title)
        if data is None:
            return Response("can't found this article")
        allowed_tags = ['a', 'abbr', 'acronym', 'b',
                        'blockquote', 'code', 'em',
                        'i', 'li', 'ol', 'pre', 'strong',
                        'ul', 'h1', 'h2', 'h3', 'p', 'br', 'ins', 'del']
        return render_to_response('article.html',{
            'titile': data.title,
            'context': markdown.markdown(data.context, output_format='html', extensions=['nl2br', 'del_ins'], tags=allowed_tags, strip=True)
        })

    def post(self, request):
        return Response({'post': 'word'})
