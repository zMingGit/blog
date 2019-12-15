# coding: utf-8
from django.contrib import admin
from blog.link.models import Link


class LinkAdmin(admin.ModelAdmin):
    model = Link
    list_display = ['uuid', 'name', 'url']


admin.site.register(Link, LinkAdmin)
