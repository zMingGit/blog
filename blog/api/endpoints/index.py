from django.shortcuts import render
from rest_framework.views import APIView

from .throttling import NoThrottling
from .authentication import MethodAuthentication
from blog.article.models import Article


class IndexView(APIView):
    throttling_classes = (NoThrottling, )
    authentication_classes = (MethodAuthentication, )
    permission_classes = ()

    def get(self, request):
        page = request.GET.get('page', 1)
        index = True
        if not isinstance(page, int) or page is None:
            pass
            
        page = int(page)
        more = False
        back = False
        if page > 1:
            index = False
            start = (page - 2 ) * 5 +4
            end = (page - 1) * 5 + 4
            articles = Article.objects.get_index_articles(start, end+1)
            back = True
        else:
            articles = Article.objects.get_index_articles(0, 5)

        if len(articles) == 6:
            more = True
        

        return render(request, "index.html", {
            'articles': articles,
            'page': page,
            'index': index,
            'back': back,
            'more': more
        })
