# coding: utf-8
from __future__ import absolute_import
from django.contrib import admin
from blog.item.models import Item, ReaderItem


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ['uuid', 'content', 'content_origin', 'create_time']


class ReaderItemAdmin(admin.ModelAdmin):
    model = ReaderItem
    list_display = ['uuid', 'ip', 'ua', 'item_content_prefix', 'create_time']

    def item_content_prefix(self):
        return self.item.content[:10]


admin.site.register(Item, ItemAdmin)
admin.site.register(ReaderItem, ReaderItemAdmin)
