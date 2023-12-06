from django import urls
from django.urls import path
import pyrebase

from . import views
app_name = 'client'
urlpatterns = [
    # path("", views.index, name="index"),
    # path("sign_in", views.signIn, name="index")/,
    path("dashboard/", views.dashboardClient, name="dashboardClient"),
    path("dashboard-non", views.dashboardClientNone, name="dashboard-client-non"),

    path("output-scenario", views.outputScenario, name="output-scenario"),
    path("detail-history", views.detailHistory, name="detail-history"),
    path('base', views.base, name='base'),
    path('baseSignIn', views.baseSignIn, name='base-signin'),

    path('history', views.history, name='history'),
    path('user-profile', views.userProfile, name='user-profile'),
    path('edit-profile', views.editProfile, name='edit-profile'),
    path('posteditprofile/', views.posteditprofile),

    # Input User Story
    path('inputUserStory', views.inputUserStory, name='inputUserStory'),
    path('postInputStory/', views.postInputStory),


    # Registration & Login

    path('', views.signin, name='signin'),
    path('postsignin/', views.postsignin),
    path('signin', views.signin, name='signin'),

    path('regist', views.regist, name='regist'),
    path('postsignup/', views.postsignup),
    

    path('signout', views.signout, name='signout'),

    # Forgot Password

    path('reset', views.reset, name='reset'),
    path('send', views.send, name='send'),
    path('postreset/', views.postreset, name='postreset')

    #
]
