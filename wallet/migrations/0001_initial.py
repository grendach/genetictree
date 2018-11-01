# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-21 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_name', models.CharField(max_length=50)),
                ('currency_country', models.FileField(upload_to='')),
                ('currency_code', models.CharField(max_length=10)),
                ('currency_symbol', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_date', models.DateField(default=None, verbose_name='Date')),
                ('expense_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expense_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Category')),
                ('expense_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_date', models.DateField(default=None, verbose_name='Date')),
                ('income_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('income_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Category')),
                ('income_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Currency')),
            ],
        ),
    ]