from django.shortcuts import render
import pyrebase
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.cache import never_cache

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


def logout(request):
    try:
        del request.session['uid']
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
    except Exception as e:
        messages.error(request, f'Registration Failed. {str(e)}')
        return redirect('client:regist')
    messages.success(request, 'Registration Success')
    return redirect('client:signin')


def reset(request):
    return render(request, 'reset.html')


def postreset(request):
    email = request.POST.get('email')
    try:
        auth.send_password_reset_email(email)
        messages.success(request, 'An Email to Reset Password has been sent')
        return redirect('client:reset', {'msg': messages})
    except:
        messages.error(
            request, 'Something went wrong, Please re-check the email you provided')
        return redirect('client:reset', {'msg': messages})


# Create your views here.


def dashboardClient(request):
    return render(request, 'client-dashboard.html')


def dashboardClientNone(request):
    return render(request, 'client-dashboard-non.html')


def detailHistory(request):
    return render(request, 'history/history-detail.html')


def base(request):
    return render(request, 'base.html')


def baseSignIn(request):
    return render(request, 'base_signin.html')


def outputScenario(request):
    return render(request, 'output-user-scenario/output_scenario.html')


def inputUserStory(request):
    return render(request, 'input-user/input.html')


def history(request):
    return render(request, 'history/history.html')


def userProfile(request):
    return render(request, 'user_profile/user-profile.html')
