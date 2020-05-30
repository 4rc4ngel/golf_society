# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-05-30 18:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('golf_app', '0003_auto_20200530_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 30, 18, 29, 57, 197037, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]
