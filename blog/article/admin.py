from django.contrib import admin
from blog.article.models import Article, ArticleType


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ['uuid', 'title', 'intro', 'context', 'article_type', 'create_time', 'image']


class ArticleTypeAdmin(admin.ModelAdmin):
    model = ArticleType
    list_display = ['uuid', 'atype']


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
