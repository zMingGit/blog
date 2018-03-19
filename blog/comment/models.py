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

    def add_comment(self, article, ip, dt, comment):
        articleObj = Article.objects.get_article_by_id(article)
        cmt = self.model(article=articleObj, ipaddress=ip, time=dt, context=comment)
        cmt.save()
        

class Comment(models.Model):
    article = models.ForeignKey(Article)
    ipaddress = models.GenericIPAddressField()
    time = models.DateTimeField()
    context = models.CharField(max_length=120)
    objects = CommentManager()
