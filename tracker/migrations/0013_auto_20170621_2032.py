# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-22 03:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_auto_20170621_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='benchmovement',
            old_name='chains',
            new_name='chain_weight',
        ),
    ]