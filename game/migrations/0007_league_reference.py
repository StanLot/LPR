# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20170803_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='reference',
            field=models.CharField(default='E50HXETXHPPDYIH', max_length=20),
        ),
    ]
