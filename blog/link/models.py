# coding: utf-8
from __future__ import absolute_import
import uuid

from django.db import models


class LinkManager(models.Manager):
    def get_all(self):
        return super(LinkManager, self).all()


class Link(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=150)
    objects = LinkManager()
