# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_auto_20170809_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='league',
            name='reference',
            field=models.CharField(default='4H5QA4D2EC5IRC9', max_length=20),
        ),
    ]