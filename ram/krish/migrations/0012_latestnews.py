# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-13 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krish', '0011_testinomials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Latestnews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
