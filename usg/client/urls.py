from django.urls import path

from . import views
app_name = 'client'
urlpatterns = [
    # path("", views.index, name="index"),
    # path("sign_in", views.signIn, name="index")/,
    path('base',views.base, name='index'),
    path('baseSignIn',views.baseSignIn, name='index'),
    path('signin',views.SignIn, name='index'),
]