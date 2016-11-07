# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FLLapp', '0007_auto_20161105_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isBoy', models.PositiveSmallIntegerField(default=3)),
                ('species', models.PositiveSmallIntegerField(default=4)),
                ('domestic', models.BooleanField(default=False)),
            ],
        ),
    ]