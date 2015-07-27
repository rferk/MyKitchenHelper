# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name_plural': 'inventory items', 'ordering': ['item'], 'verbose_name': 'inventory item'},
        ),
        migrations.AddField(
            model_name='inventory',
            name='item',
            field=models.OneToOneField(null=True, to='items.Item', blank=True),
        ),
    ]
