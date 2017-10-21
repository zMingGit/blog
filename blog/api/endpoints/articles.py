from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from rest_framework.views import APIView

from .throttling import NoThrottling
from .authentication import MethodAuthentication
from blog.article.models import Article


class ArticlesView(APIView):
    throttle_classes = (NoThrottling, )
    authentication_classes = (MethodAuthentication, )
    permission_classes = ()

    def get(self, request):
        limit = request.GET.get('limit', '').lower()
        if not limit:
            return HttpResponseRedirect(reverse("index"))

        article_types = Article.objects.get_all_article_type()
        articles = Article.objects.get_articles_by_type(limit)
        recommonds = articles
        return render_to_response("index.html", {
            'SITE_ROOT': 'qwe',
            'article_types': article_types,
            'articles': articles,
            'recommonds': recommonds
        })
