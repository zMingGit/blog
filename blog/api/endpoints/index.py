from django.shortcuts import render_to_response
from rest_framework.views import APIView

from .throttling import NoThrottling
from .authentication import MethodAuthentication
from blog.article.models import Article


class IndexView(APIView):
    throttling_classes = (NoThrottling, )
    authentication_classes = (MethodAuthentication, )
    permission_classes = ()

    def get(self, request):
        articles = Article.objects.get_index_articles()
        article_types = Article.objects.get_all_article_type()
        return render_to_response("index.html", {
            'SITE_ROOT': 'qwe',
            'article_types': article_types,
            'articles': articles,
            'title': 'Z-M'
        })
