from django.db import models

from blog.article.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article)
    name = models.CharField(max_length=30)
    time = models.DateTimeField()
    context = models.TextField()
