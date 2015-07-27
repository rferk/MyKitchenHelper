# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import items.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', items.models.LowercaseCharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', items.models.LowercaseCharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'item categories',
                'verbose_name': 'item category',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(null=True, blank=True, to='items.ItemCategory'),
        ),
    ]
