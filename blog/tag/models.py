from django.db import models

from blog.article.models import Article


class Tag(models.Model):
    name = models.CharField(max_length=50)


class ArticleTagMap(models.Model):
    article = models.ForeignKey(Article)
    tag = models.ForeignKey(Tag, db_index=True)
