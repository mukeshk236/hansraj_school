from django.conf.urls import url , include

from . import views

urlpatterns = [
    url(r'^gallery', views.gallery_view, name='gallery'),
    url(r'^', views.index, name='index'),
]