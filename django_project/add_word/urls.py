# dict/urls.py
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('dicta/', views.add_word),
    path('add_word/', views.add_word),
]
