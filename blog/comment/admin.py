from django.contrib import admin
from blog.comment.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display    = ['article', 'name', 'email', 'time', 'context', 'avatar', 'agreed', 'against']


admin.site.register(Comment, CommentAdmin)
