# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-26 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0026_remove_benchmovement_standard'),
    ]

    operations = [
        migrations.AddField(
            model_name='squatmovement',
            name='reverse',
            field=models.BooleanField(default=False),
        ),
    ]