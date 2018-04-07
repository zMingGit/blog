from django.contrib import admin
from blog.article.models import Article, ArticleType


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ['uuid', 'title', 'intro', 'context', 'article_type', 'create_time', 'image']

admin.site.register(Article, ArticleAdmin)
