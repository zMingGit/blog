from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.http import urlencode

from blog.article.models import Article

class LatestEntriesFeed(Feed):
    title = "ZMing articles"
    link = "/articles/"
    description = ""

    def items(self):
        return Article.objects.order_by('-create_time')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.context[:50] + '...'

    def item_link(self, item):
        return u'%s?%s' % (reverse('api-article'), urlencode({'uuid': item.uuid}))
