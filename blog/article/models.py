import uuid
import datetime
import markdown
import django.utils.timezone as timezone

from django.db import models
from django.db.models import Count
from blog.api.endpoints.constant import ALLOWED_TAGS


class ArticleManager(models.Manager):
    def get_article_by_id(self, input_uuid):
        try:
            input_uuid = uuid.UUID('{' + input_uuid + '}')
            article = super(ArticleManager, self).get(uuid=input_uuid)
            article.title = markdown.markdown(article.title,
                                              output_format='html',
                                              extensions=['nl2br',
                                                          'del_ins'],
                                              tags=ALLOWED_TAGS,
                                              strip=True)
            article.context = markdown.markdown(article.context,
                                                output_format='html',
                                                extensions=['nl2br',
                                                            'del_ins'],
                                                tags=ALLOWED_TAGS,
                                                strip=True)
            article.context = article.context.replace('<code>', '<pre>')
            article.context = article.context.replace('</code>', '</pre>')
            return article
        except self.model.DoesNotExist:
            return None

    def get_article_by_title(self, title):
        try:
            article = super(ArticleManager, self).get(title=title)
            article.title = markdown.markdown(article.title,
                                              output_format='html',
                                              extensions=['nl2br',
                                                            'del_ins'],
                                              tags=ALLOWED_TAGS,
                                              strip=True)
            article.context = markdown.markdown(article.context,
                                                output_format='html',
                                                extensions=['nl2br',
                                                            'del_ins'],
                                                tags=ALLOWED_TAGS, strip=True)
            article.context = article.context.replace('<code>', '<pre>')
            article.context = article.context.replace('</code>', '</pre>')
            return article
        except self.model.DoesNotExist:
            return None

    def get_index_articles(self, start, end):
        articles = super(ArticleManager, self).order_by('-create_time')[start: end]
        for article in articles:
            article.title = markdown.markdown(article.title,
                                              output_format='html',
                                              extensions=['nl2br',
                                                          'del_ins'],
                                              tags=ALLOWED_TAGS,
                                              strip=True)
            article.context = markdown.markdown(article.context,
                                                output_format='html',
                                                extensions=['nl2br',
                                                            'del_ins'],
                                                tags=ALLOWED_TAGS, strip=True)
            article.context = article.context.replace('<code>', '<pre>')
            article.context = article.context.replace('</code>', '</pre>')
            article.create_time = (datetime.datetime.now().replace(tzinfo=None) - article.create_time.replace(tzinfo=None)).days
        return articles

    def get_all_article_type(self):
        return super(ArticleManager, self).values_list('article_type',
                                                       flat=True).distinct()

    def get_all_article_type_and_count(self):
        return super(ArticleManager, self).values_list('article_type').annotate(Count('uuid'))

    def get_articles_by_type(self, article_type):
        articles = super(ArticleManager, self).filter(article_type=article_type).order_by('-create_time')[:6]
        for article in articles:
            article.title = markdown.markdown(article.title,
                                              output_format='html',
                                              extensions=['nl2br',
                                                          'del_ins'],
                                              tags=ALLOWED_TAGS,
                                              strip=True)
            article.context = markdown.markdown(article.context,
                                                output_format='html',
                                                extensions=['nl2br',
                                                            'del_ins'],
                                                tags=ALLOWED_TAGS, strip=True)
            article.context = article.context.replace('<code>', '<pre>')
            article.context = article.context.replace('</code>', '</pre>')
        return articles

class Article(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100, db_index=True)
    intro = models.TextField()
    context = models.TextField()
    article_type = models.CharField(max_length=30)
    create_time = models.DateTimeField(default=timezone.now)
    image = models.CharField(max_length=90)
    objects = ArticleManager()
