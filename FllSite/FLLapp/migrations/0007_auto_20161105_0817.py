# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FLLapp', '0006_center_siteurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='center',
            name='phone1',
        ),
        migrations.RemoveField(
            model_name='center',
            name='phone2',
        ),
        migrations.RemoveField(
            model_name='center',
            name='phone3',
        ),
        migrations.AddField(
            model_name='center',
            name='phone',
            field=models.CharField(default='No phone number found - Try checking their website', max_length=10),
        ),
    ]
