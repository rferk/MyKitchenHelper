# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveSmallIntegerField(default='1')),
                ('tracked', models.BooleanField(default=0)),
                ('threshold', models.PositiveSmallIntegerField(default='0')),
            ],
        ),
    ]
