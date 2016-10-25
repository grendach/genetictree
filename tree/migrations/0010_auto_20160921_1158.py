# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0009_auto_20160920_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='person_age',
            new_name='person_date_birth',
        ),
        migrations.AddField(
            model_name='person',
            name='person_date_death',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
