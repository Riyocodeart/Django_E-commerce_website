from django.contrib import admin
from django.urls import path
from . import views     #added 

urlpatterns = [
    path("", views.index, name='Home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact')
    
]
