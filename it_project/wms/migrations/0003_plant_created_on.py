# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0002_auto_20170829_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
