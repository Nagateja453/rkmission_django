# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-11 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krish', '0007_auto_20190911_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpost',
            name='Memorial',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='addpost',
            name='Parents',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='addpost',
            name='Place_Of_Death',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='addpost',
            name='Religious_Views',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='addpost',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
