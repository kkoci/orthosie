# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 02:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0002_auto_20151206_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=15)),
                ('scale', models.DecimalField(decimal_places=4, max_digits=19, null=True)),
                ('description', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=17)),
                ('status', models.CharField(default='ACTIVE', max_length=8)),
                ('item', models.ForeignKey(on_delete=models.CASCADE, to='inventory.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateTimeField(auto_now=True)),
                ('finish_date', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ['begin_date'],
            },
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=17)),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateTimeField()),
                ('finish_date', models.DateTimeField(null=True)),
                ('status', models.CharField(default='Started', max_length=10)),
                ('shift', models.ForeignKey(on_delete=models.CASCADE, to='register.Shift')),
            ],
            options={
                'ordering': ['begin_date'],
            },
        ),
        migrations.AddField(
            model_name='tender',
            name='transaction',
            field=models.ForeignKey(on_delete=models.CASCADE, to='register.Transaction'),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='transaction',
            field=models.ForeignKey(on_delete=models.CASCADE, to='register.Transaction'),
        ),
    ]
