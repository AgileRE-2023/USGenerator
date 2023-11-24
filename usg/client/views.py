from django.shortcuts import render
import pyrebase
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# from django.contrib import auth
from django.core import serializers
from client.models import User
from django.views.decorators.cache import never_cache
from django.contrib import messages
# import json

# Create your views here.
config = {
    'apiKey': "AIzaSyA0vBvWec1huC34E048rzWtUwkKd5bfAxU",
    'authDomain': "usg-django-pplprak.firebaseapp.com",
    'databaseURL': "https://usg-django-pplprak-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "usg-django-pplprak",
    'storageBucket': "usg-django-pplprak.appspot.com",
    'messagingSenderId': "1048754184838",
    'appId': "1:1048754184838:web:16794aa3970c3b8dd2a707",
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


def signin(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are Already Logged in.')
        return redirect('client:dashboardClient')
    return render(request, 'signin-reg/signin.html')


@login_required
def home(request):
    return render(request, 'client-dashboard.html')


def regist(request):
    return render(request, 'signin-reg/regist.html')


@never_cache
def postsignin(request):
    email = request.POST.get('email')
    passwrd = request.POST.get('password')
    try:
        user = auth.sign_in_with_email_and_password(email, passwrd)
    except:
        messages.error(request, 'Invalid Email or Password')
        return render(request, 'signin-reg/signin.html', {'email': email})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    messages.success(request, 'Login Success')
    return redirect('client:dashboardClient')


@login_required
def signout(request):
    try:
        auth.current_user = None
    except:
        pass
    messages.success(request, 'Logout Completed')
    return redirect('client:signin')


def postsignup(request):
    email = request.POST.get('email')
    passs = request.POST.get('password')
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    try:
        user = auth.create_user_with_email_and_password(email, passs)
        db.child("users").child(user['localId']).set(
            {"email": email, "name": name, "phone": phone})
    except:
        message = "invalid credentials"
        return redirect('client:regist', {'message': message})
    return redirect('client:signin')


def send(request):
    return render(request, 'signin-reg/send.html')


def reset(request):
    return render(request,'signin-reg/send.html')



def postreset(request):
    email = request.POST.get('email')
    try:
        auth.send_password_reset_email(email)
        messages.success(request, 'An Email to Reset Password has been sent')
        return redirect('client:signin')
    except:
        messages.error(
            request, 'Something went wrong, Please re-check the email you provided')
        return redirect('client:reset')


# Create your views here.
@login_required
def dashboardClient(request):
    return render(request, 'client-dashboard.html')


@login_required
def dashboardClientNone(request):
    return render(request, 'client-dashboard-non.html')


@login_required
def detailHistory(request):
    return render(request, 'history/history-detail.html')


@login_required
def base(request):
    return render(request, 'base.html')


@login_required
def baseSignIn(request):
    return render(request, 'base_signin.html')


@login_required
def outputScenario(request):
    return render(request, 'output-user-scenario/output_scenario.html')


@login_required
def inputUserStory(request):
    return render(request, 'input-user/input.html')


@login_required
def history(request):
    return render(request, 'history/history.html')


@login_required
def userProfile(request):
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    # user.fromJson(users_by_name)
    return render(request, 'user_profile/user-profile.html', {'user': users_value.val()})
