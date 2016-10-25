# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 09:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=250)),
                ('family_location', models.CharField(max_length=250)),
                ('family_logo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('second_name', models.CharField(max_length=250)),
                ('person_photo', models.CharField(max_length=1000)),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tree.Family')),
            ],
        ),
    ]