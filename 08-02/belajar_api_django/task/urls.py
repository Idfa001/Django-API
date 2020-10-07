from django.contrib import admin
from django.urls import path
from django.shortcuts import render


from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('<id>/', views.detail),
    path('<id>/update', views.update),
    path('<id>/delete', views.delete),
]