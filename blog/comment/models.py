import datetime

from django.db import models

from blog.article.models import Article


class CommentManager(models.Manager):
    def get_comment_by_page(self, uuid, page):
        start = (page - 1) * 10
        end = page * 10
        comments = super(CommentManager, self).filter(article__uuid=uuid).order_by('time')[start: end]
        for c in comments:
            c.time = c.time.strftime('%Y-%m-%d %H:%M:%S')
        return comments

    def add_comment(self, article, ip, dt, nickname, comment, email):
        self.model(article=article, ipaddress=ip, time=dt, context=comment, nickname=nickname, email=email).save()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ipaddress = models.GenericIPAddressField()
    time = models.DateTimeField()
    context = models.CharField(max_length=120)
    objects = CommentManager()
    nickname = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=30, default='')
