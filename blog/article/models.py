import uuid

from django.db import models

class ArticleManager(models.Manager):
    def get_article_by_id(self, input_uuid):
        try:
            input_uuid = uuid.UUID('{' + input_uuid + '}')
            return super(ArticleManager, self).get(uuid=input_uuid)
        except self.model.DoesNotExist:
            return None

    def get_article_by_title(self, title):
        try:
            return super(ArticleManager, self).get(title=title)
        except self.model.DoesNotExist:
            return None


class Article(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    context = models.TextField()
    objects = ArticleManager()
