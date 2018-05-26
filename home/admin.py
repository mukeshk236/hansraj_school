# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import notice,job_application,gallery

# Register your models here.

class notice_admin(admin.ModelAdmin):
    fields = [ 'title','image', 'description', 'time' , 'status']
    list_display = ('title', 'image', 'description' , 'time' , 'status')

class job_application_admin(admin.ModelAdmin):
    fields = ['name', 'phone']
    list_display = ('name', 'phone')

class gallery_admin(admin.ModelAdmin):
    fields = ['category', 'event','image', 'description','status']
    list_display = ('category', 'event', 'image','description','status')

admin.site.register(notice , notice_admin)
admin.site.register(job_application, job_application_admin)
admin.site.register(gallery , gallery_admin)