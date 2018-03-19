from django.conf.urls import url


from .views import *
from .endpoints.index import IndexView
from .endpoints.article import ArticleView, CommentView

urlpatterns = [
    url(r'ping/$', Ping.as_view(), name='api-ping'),
    url(r'index/$', IndexView.as_view(), name='api-index'),
    url(r'article/$', ArticleView.as_view(), name='api-article'),
    url(r'comment/$', CommentView.as_view(), name='api-comment'),
]
