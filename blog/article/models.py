import uuid
from markdown import markdown
import django.utils.timezone as timezone
from collections import Iterable

from django.db import models
from django.db.models import Count
from blog.api.endpoints.constant import ALLOWED_TAGS
from blog.article.const import RecordType


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

    def add_record_time(self, article_uuid, record_type):
        article = super(ArticleManager, self).get(uuid=article_uuid)
        if record_type == RecordType.VISIT:
            article.n_visits = models.F('n_visits') + 1
        elif record_type == RecordType.COMMENT:
            article.n_comments = models.F('n_comments') + 1
        article.save()


class ArticleStatsRecord(models.Manager):
    def create_visit_record(self, article, ip, ua):
        record_type = RecordType.VISIT
        self.model(uuid=uuid.uuid4(), ip=ip, ua=ua, article=article, record_type=record_type).save()
        Article.objects.add_record_time(article.uuid, record_type)

    def create_comment_record(self, article, ip, ua):
        record_type = RecordType.COMMENT
        self.model(uuid=uuid.uuid4(), ip=ip, ua=ua, article=article, record_type=record_type).save()
        Article.objects.add_record_time(article.uuid, record_type)


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
    n_visits = models.IntegerField(default=0)
    n_comments = models.IntegerField(default=0)
    image = models.CharField(max_length=90)
    objects = ArticleManager()


class ArticleStatsRecord(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    ip = models.GenericIPAddressField()
    ua = models.CharField(max_length=100)
    record_type = models.IntegerField()
    article = models.ForeignKey('Article', on_delete=models.PROTECT)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)
    objects = ArticleStatsRecord()
