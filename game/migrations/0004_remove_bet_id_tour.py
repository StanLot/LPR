# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20170730_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='id_tour',
        ),
    ]