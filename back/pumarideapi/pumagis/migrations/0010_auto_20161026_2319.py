# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 23:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pumagis', '0009_auto_20161023_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='line',
            name='name',
        ),
        migrations.RemoveField(
            model_name='point',
            name='name',
        ),
    ]
