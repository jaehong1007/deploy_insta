# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, verbose_name='나이'),
        ),
        migrations.AlterField(
            model_name='user',
            name='like_posts',
            field=models.ManyToManyField(blank=True, to='post.Post', verbose_name='좋아요 누른 포스트 목록'),
        ),
    ]