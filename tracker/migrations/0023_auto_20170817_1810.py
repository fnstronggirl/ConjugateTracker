# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-18 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0022_auto_20170817_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadliftmovement',
            name='created_at',
            field=models.DateTimeField(blank=True),
        ),
    ]