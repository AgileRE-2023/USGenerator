from django.urls import path

from . import views

app_name = 'admin_site'
urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('user', views.user, name='index'),
=======
    path('projectview', views.projectView, name='projectview')
>>>>>>> admin-project-view
]