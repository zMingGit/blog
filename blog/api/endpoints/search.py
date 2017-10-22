from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from rest_framework.views import APIView

from .throttling import NoThrottling
from .authentication import MethodAuthentication
from blog.article.models import Article


class SearchView(APIView):
    throttling_classes = (NoThrottling, )
    authentication_classes = (MethodAuthentication, )
    permission_classes = ()

    def get(self, request):
        search_test = request.GET.get('contains', '')
        if not search_test:
            return HttpResponseRedirect(reverse("index"))
        articles = Article.objects.get_articles_by_search(search_test)
        article_types = Article.objects.get_all_article_type()
        return render_to_response("index.html", {
            'SITE_ROOT': 'qwe',
            'article_types': article_types,
            'articles': articles,
            'title': 'Z-M | Search'
        })
