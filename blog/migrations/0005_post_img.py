# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-31 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190327_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.TextField(default=''),
        ),
    ]
