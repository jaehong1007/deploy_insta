# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20171114_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True, verbose_name='나이'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=10, null=True, verbose_name='별명'),
        ),
    ]
