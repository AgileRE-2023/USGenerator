from django.urls import path

from . import views
app_name = 'client'
urlpatterns = [
    # path("", views.index, name="index"),
    # path("sign_in", views.signIn, name="index")/,
    path("output-scenario", views.outputScenario, name="output-scenario"),
    path("detail-history", views.detailHistory, name="detail-history"),
    path('base', views.base, name='base'),
    path('baseSignIn', views.baseSignIn, name='base-signin'),
    path('signin', views.SignIn, name='signin'),
    path('regist', views.regist, name='regist'),
    path('inputUserStory', views.inputUserStory, name='inputUserStory'),
    path('history', views.history, name='history')
]
