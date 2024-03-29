# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-12 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krish', '0009_addpage_excerpt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imageshow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image_field_1', models.FileField(blank=True, null=True, upload_to='mission_pics')),
                ('image_field_2', models.FileField(blank=True, null=True, upload_to='mission_pics')),
                ('image_field_3', models.FileField(blank=True, null=True, upload_to='mission_pics')),
                ('image_field_4', models.FileField(blank=True, null=True, upload_to='mission_pics')),
                ('image_field_5', models.FileField(blank=True, null=True, upload_to='mission_pics')),
                ('image_field_6', models.FileField(blank=True, null=True, upload_to='mission_pics')),
                ('gallery', models.CharField(choices=[('nature', 'nature'), ('landscape', 'landscape')], max_length=50, null=True)),
            ],
        ),
    ]
