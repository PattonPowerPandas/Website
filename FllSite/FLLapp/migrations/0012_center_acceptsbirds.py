# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FLLapp', '0011_auto_20161105_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='acceptsbirds',
            field=models.BooleanField(default=False),
        ),
    ]
