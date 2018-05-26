# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import os
from django.conf import settings

status = (
	("ACTIVE", "active"),
	("NOT_ACTIVE", "not active"),
)
event_choice = (
	("NONE", "none"),
	("HAPPY NEW YEAR", "happy new year"),
	("HAPPY HOLI", "happy holi"),
)
category_choice = (
	("PRIMARY", "primary"),
	("SECONDARY", "secondary"),
	("SENIOR", "senior"),
)
# Create your models here.
class notice(models.Model):
	image = models.ImageField(upload_to = "images/notice/", blank=True)
	menu_image_name = models.CharField(max_length = 200)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	time = models.DateTimeField('date published')
	status = models.CharField(max_length=10,choices= status,default="ACTIVE")
	def __unicode__(self):
		return unicode(self.menu_image_name)
class job_application(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=10)

class gallery(models.Model):
	image = models.ImageField(upload_to = "images/gallery/", blank=True) 
	category = models.CharField(max_length=50,choices= category_choice,default="PRIMARY")
	event = models.CharField(max_length=50,choices= event_choice,default="NONE")
	description = models.CharField(max_length=500)
	status = models.CharField(max_length=10,choices= status,default="ACTIVE")
