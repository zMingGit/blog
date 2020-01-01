# coding: utf-8
from __future__ import absolute_import
import sys
import uuid
import random

from django.db import models


class ItemManager(models.Manager):
    def get_all(self):
        return super(ItemManager, self).all()


class Item(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    content = models.TextField()
    content_origin = models.CharField(max_length=120)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)
    objects = ItemManager()


class ReaderItemManager(models.Manager):
    def get_one(self, ip):
        items = Item.objects.get_all()
        consumed_uuid_list = [item['item'] for item in super(ReaderItemManager, self).filter(ip=ip).values('item')]
        items = [item for item in items if item.uuid not in consumed_uuid_list]
        if items:
            return random.choice(items)

    def get_by_ip_and_item(self, ip, item):
        return super(ReaderItemManager, self).filter(ip=ip, item=item.uuid)

    def read_item(self, item, ip, ua):
        try:
            print('get')
            super(ReaderItemManager, self).get(ip=ip, item=item)
        except self.model.DoesNotExist:
            print('save')
            item = self.model(uuid=uuid.uuid4(), ip=ip, ua=ua, item=item)
            item.save()


class ReaderItem(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['ip'])
        ]
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    ip = models.GenericIPAddressField()
    ua = models.CharField(max_length=100)
    item = models.ForeignKey('Item', on_delete=models.PROTECT)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)
    objects = ReaderItemManager()
