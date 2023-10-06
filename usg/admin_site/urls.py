from django.urls import path
from django.urls import re_path as url
from . import views

app_name = 'admin_site'
urlpatterns = [
    path('', views.index, name='index'),
    path('user', views.user, name='user'),
    path('projectview', views.projectView, name='projectview'),
    path('dashboard', views.dashboard, name='dashboard')
]
