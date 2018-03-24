from django.shortcuts import render
from rest_framework.views import APIView

from .throttling import NoThrottling
from .authentication import MethodAuthentication
from blog.article.models import Article


def safe_trans_to_int(x):
    try:
        return int(x)
    except:
        return x

class IndexView(APIView):
    throttling_classes = (NoThrottling, )
    authentication_classes = (MethodAuthentication, )
    permission_classes = ()

    def get(self, request):
        page = safe_trans_to_int(request.GET.get('page', 1))
        search_text = request.GET.get('search_text', None)
        spec_msg = ""
        index = True
        if not isinstance(page, int) or page is None:
            spec_msg = "parameter invalid."
            return render(request, "index.html", {
                'spec_msg': spec_msg
            })
            
        page = int(page)
        more = False
        back = False
        if page > 1:
            index = False
            start, end = (page - 2 ) * 5 +4, (page - 1) * 5 + 4
            back = True
            count = 6
        else:
            count = 5
            start, end = 0, 4

        if search_text:
            articles = Article.objects.get_articles_by_search(search_text, start, end+1)
            index = False
            reduce_one = False
            if len(articles) == 0:
                spec_msg = "There is no matching result."
        else:
            articles = Article.objects.get_index_articles(start, end+1)
            reduce_one = True
       
        if len(articles) == count:
            more = True

        if reduce_one and len(articles) == count:
            articles = articles[:-1]


        return render(request, "index.html", {
            'articles': articles,
            'page': page,
            'index': index,
            'back': back,
            'more': more,
            'spec_msg': spec_msg
        })
