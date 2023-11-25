from django.shortcuts import render
import pyrebase
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core import serializers
from client.models import UserStory
import uuid
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
    return render(request, 'signin-reg/signin.html')


@login_required
def home(request):
    return render(request, 'client-dashboard.html')


def regist(request):
    return render(request, 'signin-reg/regist.html')

def postsignin(request):
    email = request.POST.get('email')
    passwrd = request.POST.get('password')
    try:
        user = auth.sign_in_with_email_and_password(email, passwrd)
    except:
        message = "Invalid Email or Password"
        return render(request, 'signin-reg/signin.html', {'email': email})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    message = 'Login Success'
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}/userstories').get()
    UserStory_values=users_value.val()
    print(UserStory_values)
    return render(request, "client-dashboard.html", {'message': message,'UserStory_values': UserStory_values})

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, 'signin-reg/signin.html')

def postsignup(request):
    email = request.POST.get('email')
    passs = request.POST.get('password')
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    try:
        user = auth.create_user_with_email_and_password(email, passs)
        db.child("users").child(user['localId']).set({"email": email, "name": name, "phone": phone})
    except:
        return render(request, 'signin-reg/regist.html')
    return render(request, 'signin-reg/signin.html')

def reset(request):
    return render(request, 'signin-reg/send.html')

def postreset(request):
    email = request.POST.get('email')
    try:
        auth.send_password_reset_email(email)
        message = "An email to reset password is successfully sent"
        return render(request, 'signin-reg/reset.html', {'msg': message})
    except:
        message = "Something went wrong, Please re-check the email you provided"
        return render(request, 'signin-reg/reset.html', {'msg': message})



def dasboardClient(request):
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}/userstories').get()
    UserStory_values=users_value.val()
    print(UserStory_values)
    return render(request, 'client-dashboard.html', {'UserStory_values': UserStory_values})


def dasboardClientNone(request):
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

# def postInputStory(request):
#     ProjectTitle = request.POST.get('ProjectTitle')
#     inputParagraf = request.POST.get('inputParagraf')
#     idtoken=request.session['uid']
#     a=auth.get_account_info(idtoken)
#     a=a['users']
#     # a=a[0]
#     a=a[0]['localId']
#     print(str(a))
#     data= {
#         'userStory' : {
#             "ProjectTitle":ProjectTitle,
#             "inputParagraf":inputParagraf
#         }
#     }
#     db.child('users').child(str(a)).update(data)
    
#     # result = db.put('/UserStory', UserStory, data)
#     return render(request, 'input-user/input.html')

def postInputStory(request):
    ProjectTitle = request.POST.get('ProjectTitle')
    inputParagraf = request.POST.get('inputParagraf')
    idtoken = request.session['uid']
    user_info = auth.get_account_info(idtoken)
    
    if 'users' in user_info:
        users_list = user_info['users']
        if users_list:
            user_local_id = users_list[0].get('localId')
            print(user_local_id)
            if user_local_id:
                # data = {
                #     'userStory': {
                #         "ProjectTitle": ProjectTitle,
                #         "inputParagraf": inputParagraf
                #     }
                # }
                # data = /
                db.child('users').child(user_local_id).child('userstories').push({"ProjectTitle": ProjectTitle,"inputParagraf": inputParagraf})
                print("Data updated successfully")
                return render(request, 'input-user/input.html')



def history(request):
    return render(request, 'history/history.html')


def userProfile(request):
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    # user.fromJson(users_by_name)
    return render(request, 'user_profile/user-profile.html', {'user': users_value.val()})
