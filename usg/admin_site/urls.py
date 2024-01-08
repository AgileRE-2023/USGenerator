from django.urls import path
from . import views

app_name = 'admin'
urlpatterns = [
    path('admin/user', views.user, name='user'),
    path('admin/projectview', views.projectView, name='projectview'),
    path('admin/', views.dashboard, name='dashboard')
]
