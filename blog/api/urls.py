from django.conf.urls import url


from .views import Ping
from .endpoints.index import IndexView
from .endpoints.article import ArticleView, CommentView

urlpatterns = [
    url(r'ping/$', Ping.as_view(), name='api-ping'),
    url(r'article/$', ArticleView.as_view(), name='api-article'),
    url(r'comment/$', CommentView.as_view(), name='api-comment')
]
