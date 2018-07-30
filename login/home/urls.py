from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from home import views

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^base$', views.base,name='base'),
    url(r'^index$', views.index,name='index'),
    url(r'^add/$', views.add,name='add'),
    url(r'^imageupload/$', views.image_upload,name='imageupload'),
]
