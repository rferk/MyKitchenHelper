# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='stock',
            field=models.PositiveSmallIntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='item',
            name='threshold',
            field=models.PositiveSmallIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='item',
            name='tracked',
            field=models.BooleanField(default=0),
        ),
    ]
