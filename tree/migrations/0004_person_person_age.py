# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0003_auto_20160908_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_age',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
