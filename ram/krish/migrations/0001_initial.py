# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-09 11:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_of_Birth', models.CharField(max_length=255)),
                ('Place_Of_Birth', models.CharField(max_length=255)),
                ('Parents', models.CharField(max_length=255)),
                ('Wife', models.CharField(max_length=255)),
                ('Religious_Views', models.CharField(max_length=255)),
                ('Philosopy', models.CharField(max_length=255)),
                ('Memorial', models.CharField(max_length=255)),
                ('Place_Of_Death', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=900, null=True)),
                ('title', models.CharField(max_length=255)),
                ('excerpt', models.TextField(blank=True, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('content', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Content')),
                ('project_image1', models.FileField(blank=True, null=True, upload_to='project_logo')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
