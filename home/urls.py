from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index , name='home'),
    path("about", views.about , name='about'),
    path("blogs", views.blogs , name='blogs'),
    path("services", views.services , name='services'),
    path("contact", views.contact , name='contact'),
]

