# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20171114_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=10, verbose_name='별명'),
        ),
    ]
