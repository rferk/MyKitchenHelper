# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20150726_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(default=1, to='items.ItemCategory'),
            preserve_default=False,
        ),
    ]
