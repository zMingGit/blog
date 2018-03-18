import datetime

from django.db import models

from blog.article.models import Article


class CommentManager(models.Manager):
    def get_comment_by_page(self, uuid, page):
        start = (page - 1) * 10
        end = page * 10
        comments = super(CommentManager, self).filter(article__uuid=uuid).order_by('time')[start: end]
        for c in comments:
            c.time = (datetime.datetime.now().replace(tzinfo=None) - c.time.replace(tzinfo=None)).days
        return comments
        

class Comment(models.Model):
    article = models.ForeignKey(Article)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    time = models.DateTimeField()
    context = models.CharField(max_length=120)
    avatar = models.CharField(max_length=100)
    agreed = models.IntegerField()
    against = models.IntegerField()
    objects = CommentManager()
