from django.urls import path
from . import views
from django.contrib import admin
from django.contrib import client

app_name = 'admin'
urlpatterns = [
    path('admin/user', views.user, name='user'),
    path('projectview', views.projectView, name='projectview'),
    path('admin/', views.dashboard, name='dashboard')
]
