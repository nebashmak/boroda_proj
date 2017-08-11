from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^contact', views.contactform, name='contact'),
    url(r'^thanks', views.thanks, name='thanks'),
    url(r'^tovari/$', views.tovari, name='tovari'),
    url(r'^tovari/male', views.male, name='male'),
    url(r'^tovari/female', views.female, name='female'),
    url(r'^tovari/kids', views.kids, name='kids'),

]
