# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_id', models.CharField(max_length=50)),
                ('pwd', models.CharField(max_length=32)),
            ],
        ),
    ]