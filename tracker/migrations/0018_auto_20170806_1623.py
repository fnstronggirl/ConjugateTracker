# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-06 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0017_merge_20170720_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squatmovement',
            name='created_at',
            field=models.DateField(),
        ),
    ]
