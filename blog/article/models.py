import uuid
from markdown import markdown
import django.utils.timezone as timezone
from collections import Iterable

from django.db import models
from django.db.models import Count
from blog.api.endpoints.constant import ALLOWED_TAGS


class ArticleManager(models.Manager):
    def get_article_by_id(self, input_uuid):
        try:
            input_uuid = uuid.UUID('{' + input_uuid + '}')
            article = super(ArticleManager, self).get(uuid=input_uuid)
            return self.trans_articles(article)[0]
        except self.model.DoesNotExist:
            return None

    def get_article_by_title(self, title):
        try:
            article = super(ArticleManager, self).get(title=title)
            if len(article) > 1:
                article = article[0]
            return self.trans_articles(article)[0]
        except self.model.DoesNotExist:
            return None

    def get_index_articles(self, start, end):
        articles = super(ArticleManager, self).order_by('-create_time')[start: end]
        return self.trans_articles(articles)

    def get_articles_by_search(self, key_word, start, end):
        articles = super(ArticleManager, self).filter(context__contains=key_word).order_by('-create_time')[start: end]
        return self.trans_articles(articles)

    def trans_articles(self, articles):
        if not isinstance(articles, Iterable):
            articles = [articles]
        for article in articles:
            article.title = markdown(article.title,
                                     output_format='html',
                                     extensions=['nl2br'],
                                     tags=ALLOWED_TAGS,
                                     strip=True)
            article.context = markdown(article.context,
                                       extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite',
                                                   'markdown.extensions.sane_lists', 'pymdownx.tilde', 'pymdownx.arithmatex',
                                                   'pymdownx.keys']
                                       )
            article.create_time = article.create_time.replace(tzinfo=None).strftime('%Y-%m-%d %H:%M:%S')
        return articles

    def get_articles_by_atype(self, atype, start, end):
        articles = super(ArticleManager, self).filter(article_type=atype).order_by('-create_time')[start: end]
        return self.trans_articles(articles)

    def get_all_article_type_and_count(self):
        return super(ArticleManager, self).values_list('article_type__atype', 'article_type__uuid', ).annotate(Count('uuid'))


class ArticleType(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    atype = models.CharField(max_length=30)

    def __str__(self):
        return self.atype


class Article(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100, db_index=True)
    intro = models.TextField()
    context = models.TextField()
    article_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=timezone.now)
    image = models.CharField(max_length=90)
    objects = ArticleManager()
