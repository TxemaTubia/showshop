# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-03 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyshoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='buy_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
