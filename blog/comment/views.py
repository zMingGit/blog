# coding: utf-8
from __future__ import absolute_import

from blog.comment.models import Comment
from blog.article.models import Article, ArticleStatsRecord
from blog.comment.tasks import comment_noti


def add_comment(article_uuid, ip, ua, dt, nickname, comment, email):
    article = Article.objects.get_article_by_id(article_uuid)
    Comment.objects.add_comment(article, ip, dt, nickname, comment, email)
    ArticleStatsRecord.objects.create_comment_record(article, ip, ua)
    comment_noti.apply_async((nickname, article.title), epires=120)
