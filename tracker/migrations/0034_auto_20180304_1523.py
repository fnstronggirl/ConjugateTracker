# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-03-04 23:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0033_auto_20180304_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squatmovement',
            name='created_at',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
