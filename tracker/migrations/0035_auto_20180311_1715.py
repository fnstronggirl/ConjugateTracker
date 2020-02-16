# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-03-12 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0034_auto_20180304_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='loweraccessorymovement',
            name='kb_swings',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='loweraccessorymovement',
            name='trapbar_deadlift',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='upperaccessorymovement',
            name='pushups',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]