# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse
from .models import gallery


def index(request):
    images = gallery.objects.all()
    img_dict = {}
    for img in images:
        if img.category in img_dict:
            img_dict[img.category].append(img)
        else:
            img_dict[img.category] = [img]
    return render_to_response('index.html', {'img_dict': img_dict})


def gallery_view(request):
    images = gallery.objects.all()
    img_dict = {}
    for img in images:
        if img.category in img_dict:
            img_dict[img.category].append(img)
        else:
            img_dict[img.category] = [img]
    return render_to_response('gallery.html', {'img_dict': img_dict})