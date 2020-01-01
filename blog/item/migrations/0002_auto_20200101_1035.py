# Generated by Django 3.0 on 2020-01-01 10:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReaderItem',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('ip', models.GenericIPAddressField()),
                ('ua', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('item_uuid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='item.Item')),
            ],
        ),
        migrations.AddIndex(
            model_name='readeritem',
            index=models.Index(fields=['ip', 'item_uuid'], name='item_reader_ip_a6abed_idx'),
        ),
    ]