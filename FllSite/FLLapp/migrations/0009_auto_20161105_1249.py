# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FLLapp', '0008_animal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='isBoy',
        ),
        migrations.AddField(
            model_name='animal',
            name='gender',
            field=models.PositiveSmallIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='center',
            name='phone',
            field=models.CharField(default='Unknown', max_length=10),
        ),
    ]
