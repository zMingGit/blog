from django.contrib import admin
from blog.comment.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display    = ['article', 'ipaddress', 'time', 'context']


admin.site.register(Comment, CommentAdmin)
