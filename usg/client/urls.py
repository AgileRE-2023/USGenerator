from django.urls import path

from . import views
apps_name = 'client'
urlpatterns = [
    path("output-scenario", views.outputScenario, name="index"),
]