# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0004_person_person_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_merried',
            field=models.BooleanField(default=False),
        ),
    ]
