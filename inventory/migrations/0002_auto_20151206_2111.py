# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produce',
            name='plu',
            field=models.IntegerField(unique=True),
        ),
    ]