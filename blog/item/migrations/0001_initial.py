# Generated by Django 3.0 on 2020-01-01 09:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('content_origin', models.CharField(max_length=120)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]