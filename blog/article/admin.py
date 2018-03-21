from django.contrib import admin
from blog.article.models import Article, ArticleType


admin.site.register(Article)
admin.site.register(ArticleType)
