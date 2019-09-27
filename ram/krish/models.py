# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce import HTMLField
from django.contrib.auth.models import User

# Create your models here.

gallery = [
    ('nature','nature'),
    ('landscape','landscape'),
]

ramakrishna = [
	('About us','About us'),
	('Academics','Academics'),
	('Admissions','Admissions'),
	('Studentcorner','Studentcorner'),
	('Careers','careers'),
	('infrastructure','infrastructure'),
]

class AddPost(models.Model):
	title = models.CharField(max_length=255,null=True, blank=True)
	slug = models.SlugField(max_length=900, null=True, blank=True)
	Date_of_Birth = models.CharField(max_length=255)
	Place_Of_Birth= models.CharField(max_length=255)
	project_image1 = models.FileField(upload_to='mission_pics', null=True, blank=True)
	Parents= models.CharField(max_length=255,null=True, blank=True)
	Wife= models.CharField(max_length=255, null=True, blank=True)
	Education= models.CharField(max_length=255, null=True, blank=True)
	Spouse= models.CharField(max_length=255, null=True, blank=True)
	Guru= models.CharField(max_length=255, null=True, blank=True)
	Death= models.CharField(max_length=255, null=True, blank=True )
	Religious_Views= models.CharField(max_length=255,null=True, blank=True)
	Philosopy = models.CharField(max_length=255, null=True, blank=True)
	Memorial = models.CharField(max_length=255,null=True, blank=True)
	Place_Of_Death= models.CharField(max_length=255,null=True, blank=True)
	excerpt = models.TextField(null=True, blank=True)
	content = HTMLField('Content', null=True, blank=True)
	meta_description = models.TextField(null=True, blank=True)
	keywords = models.TextField(null=True, blank=True)
	created_by = models.ForeignKey(User, null=True, blank=True)
	modified_on = models.DateTimeField(auto_now=True)
	created_on = models.DateTimeField(auto_now=True)


	def __unicode__(self):
		return  unicode(self.title) 


class AddPage(models.Model):
	title = models.CharField(max_length=255)	
	slug = models.SlugField(max_length=900, null=True, blank=True)
	excerpt = models.TextField(null=True, blank=True)
	content = HTMLField('Content', null=True, blank=True)
	meta_description = models.TextField(null=True, blank=True)
	keywords = models.TextField(null=True, blank=True)
	ramakrishna =  models.CharField(choices=ramakrishna, max_length=50, null=True)
	created_on = models.DateTimeField(auto_now=True)
	modified_on = models.DateTimeField(auto_now=True)
	project_image2 = models.FileField(upload_to='mission_pics', null=True, blank=True)

	def __unicode__(self):
		return self.title


class Imageshow(models.Model):
	title = models.CharField(max_length=255)
	image_field_1 = models.FileField(upload_to='mission_pics', null=True, blank=True)
	image_field_2 = models.FileField(upload_to='mission_pics', null=True, blank=True)
	image_field_3 = models.FileField(upload_to='mission_pics', null=True, blank=True)
	image_field_4 = models.FileField(upload_to='mission_pics', null=True, blank=True)
	image_field_5 = models.FileField(upload_to='mission_pics', null=True, blank=True)
	image_field_6 = models.FileField(upload_to='mission_pics', null=True, blank=True)	
	gallery = models.CharField(choices=gallery, max_length=50, null=True)

	def __unicode__(self):
		return self.title


class Testinomials(models.Model):
	name = models.CharField(max_length=255,null=True, blank=True)
	title = models.CharField(max_length=255,null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.title


class Latestnews(models.Model):
	title = models.CharField(max_length=255,null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.title

class Donations(models.Model):
	title = models.CharField(max_length=255,null=True, blank=True)	
	slug = models.SlugField(max_length=900, null=True, blank=True)
	excerpt = models.TextField(null=True, blank=True)
	content = HTMLField('Content', null=True, blank=True)
	meta_description = models.TextField(null=True, blank=True)
	keywords = models.TextField(null=True, blank=True)
	created_on = models.DateTimeField(auto_now=True)
	modified_on = models.DateTimeField(auto_now=True)
	project_image2 = models.FileField(upload_to='mission_pics', null=True, blank=True)

	def __unicode__(self):
		return self.title
