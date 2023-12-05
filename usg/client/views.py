import pyrebase
# from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
# from django.contrib import auth
from django.core import serializers
from client.models import UserStory
import uuid
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.db import models

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


# @never_cache
def signin(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are Already Logged in.')
        return redirect('client:dashboardClient')
    return render(request, 'signin-reg/signin.html')


# @login_required
def home(request):
    return render(request, 'client-dashboard.html')


def regist(request):
    return render(request, 'signin-reg/regist.html')


# @never_cache
def postsignin(request):
    email = request.POST.get('email')
    passwrd = request.POST.get('password')
    try:
        user = auth.sign_in_with_email_and_password(email, passwrd)
    except:
        messages.error(request, 'Invalid Email or Password')
        return redirect('client:signin')
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return redirect('client:dashboardClient')


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
        return redirect('client:regist')
    return redirect('client:signin')


def send(request):
    return render(request, 'signin-reg/send.html')


def reset(request):
    return render(request, 'signin-reg/reset.html')


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


def resetpw(request):
    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    # user.fromJson(users_by_name)
    return render(request, 'signin-reg/signin.html', {'user': users_value.val()})

# Create your views here.


def dashboardClient(request):
    from datetime import datetime
    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    users_stories = db.child(f'users/{user_auth}/userstories').get()


    # get the id of user stories, stll dictionary need to convert to list
    users_stories_title = db.child(f'users/{user_auth}/userstories').shallow().get()
    # convert to list
    arr_users_stories_title = list(users_stories_title.val())
    # sort the id
    arr_users_stories_title.sort()


    # get the data for dashboard
    # get the ProjectTitle
    projectTitle=[]
    for i in arr_users_stories_title:
        projectTemp=db.child(f'users/{user_auth}/userstories/{i}').child('ProjectTitle').get().val()
        projectTitle.append(projectTemp)
    print(projectTitle)
    # get the user story
    userStories=[]
    for i in arr_users_stories_title:
        projectTemp=db.child(f'users/{user_auth}/userstories/{i}').child('inputParagraf').get().val()
        userStories.append(projectTemp)
    print(userStories)

    # get the time stamp
    timestamp=[]
    for i in arr_users_stories_title:
        projectTemp=db.child(f'users/{user_auth}/userstories/{i}').child('created_at').get().val()
        # projectTemp=projectTemp
        timestamp.append(projectTemp)
    # print(timestamp)
    # for i in arr_users_stories_title:
    #     i=float(i)
    #     projectTemp=datetime.datetime.fromtimestamp(i).strftime('%H-%M %d-%m-%Y')
    #     timestamp.append(projectTemp)
    print(timestamp)
    # end get data


    # zip the data
    zip_data=zip(arr_users_stories_title,projectTitle,userStories,timestamp)

    UserStory_values = users_stories.val()
    UserStory_values_title = users_stories_title.val()
    print(arr_users_stories_title)
    # user.fromJson(users_by_name)
    return render(request, 'client-dashboard.html', {'user': users_value.val(), 'UserStory_values': UserStory_values,'zip_data':zip_data})


# @login_required
def dashboardClientNone(request):
    user = request.user
    return render(request, 'client-dashboard-non.html')


# @login_required
def detailHistory(request):
    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    # user.fromJson(users_by_name)

    # get timestamp    
    # get the id of user stories, stll dictionary need to convert to list
    users_stories_title = db.child(f'users/{user_auth}/userstories').shallow().get()
    # convert to list
    arr_users_stories_title = list(users_stories_title.val())
    # sort the id
    arr_users_stories_title.sort()
    # get the time stamp
    timestamp=[]
    for i in arr_users_stories_title:
        projectTemp=db.child(f'users/{user_auth}/userstories/{i}').child('created_at').get().val()
        # projectTemp=projectTemp
        timestamp.append(projectTemp)
    print(timestamp)

    return render(request, 'history/history-detail.html', {'user': users_value.val(),'timestamp':timestamp})


# @login_required
def base(request):
    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    # user.fromJson(users_by_name)
    return render(request, 'base.html', {'user': users_value.val()})


# @login_required
def baseSignIn(request):
    user = request.user
    return render(request, 'base_signin.html')


# @login_required
def outputScenario(request):
    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    # user.fromJson(users_by_name)
    return render(request, 'output-user-scenario/output_scenario.html', {'user': users_value.val()})


# @login_required
def inputUserStory(request):
    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    # user.fromJson(users_by_name)
    return render(request, 'input-user/input.html', {'user': users_value.val()})

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


# def postInputStory(request):
#     import time
#     from datetime import datetime, timezone
#     import pytz

#     ProjectTitle = request.POST.get('ProjectTitle')
#     inputParagraf = request.POST.get('inputParagraf')
#     idtoken = request.session['uid']
#     user_info = auth.get_account_info(idtoken)
    
#     if 'users' in user_info:
#         users_list = user_info['users']
#         if users_list:
#             user_local_id = users_list[0].get('localId')
#             print(user_local_id)
#             if user_local_id:
#                 # data = {
#                 #     'userStory': {
#                 #         "ProjectTitle": ProjectTitle,
#                 #         "inputParagraf": inputParagraf
#                 #     }
#                 # }
#                 # data = /
#                 db.child('users').child(user_local_id).child('userstories').push(
#                     {"ProjectTitle": ProjectTitle, "inputParagraf": inputParagraf,"created_at":created_at})
                
#                 print("testestes")
#                 # print("Data updated successfully")
#                 return render(request, 'input-user/input.html')

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
    import time
    from datetime import datetime, timezone
    import pytz
    ProjectTitle = request.POST.get('ProjectTitle')
    inputParagraf = request.POST.get('inputParagraf')
    idtoken = request.session['uid']
    user_info = auth.get_account_info(idtoken)
    tz=pytz.timezone('Asia/Jakarta')
    created_at = datetime.now(timezone.utc).astimezone(tz).isoformat()
    print(created_at)
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
                db.child('users').child(user_local_id).child('userstories').push(
                    {"ProjectTitle": ProjectTitle, "inputParagraf": inputParagraf,"created_at":created_at})
                print("Data updated successfully")
                return render(request, 'input-user/input.html')


# @login_required
def history(request):
    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    # user.fromJson(users_by_name)
    return render(request, 'history/history.html', {'user': users_value.val()})


# @login_required
def userProfile(request):
    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    # user.fromJson(users_by_name)
    return render(request, 'user_profile/user-profile.html', {'user': users_value.val()})


def editProfile(request):
    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    # user.fromJson(users_by_name)
    return render(request, 'user_profile/edit-profile.html', {'user': users_value.val()})


def posteditprofile(request):
    # user_auth = auth.current_user['localId']
    # user = request.user
    # if request.method == 'POST':
    #     if user.is_authenticated:
    #         name = request.POST.get('name')
    #         email = request.POST.get('email')
    #         phone = request.POST.get('phone')

    #         # Assuming 'name', 'email', and 'phone' are fields in your user model
    #         db.child("users").child(f'users/{user_auth}').update({
    #             "email": email,
    #             "name": name,
    #             "phone": phone
    #         })
    #         return redirect('client:user-profile')

    # return redirect('client:edit-profile')
    # if request.method == 'POST':
    #     # Assuming you have a way to get the user ID
    #     user_auth = auth.current_user['localId']
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')

    #     # Update user profile in the Realtime Database
    #     db.child("users").child(user_auth['localId']).update({
    #         "email": email,
    #         "name": name,
    #         "phone": phone
    #     })

    #     messages.success(request, 'Profile updated successfully!')
    #     return redirect('client:user-profile')

    # return redirect('client:edit-profile')
    if request.method == 'POST':
        user_auth = auth.current_user
        if 'localId' in user_auth:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            # Update user profile in the Realtime Database
            db.child("users").child(user_auth['localId']).update({
                "email": email,
                "name": name,
                "phone": phone
            })
            messages.success(request, 'Profile updated successfully!')
            return redirect('client:user-profile')
        messages.error(request, 'Failed to update profile.')
        return redirect('client:edit-profile')
