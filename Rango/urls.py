from django.conf.urls import url
from django.contrib import admin
from Rango import views
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
]