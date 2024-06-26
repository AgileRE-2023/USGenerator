import pyrebase
import pickle
import json
# from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
# from django.contrib import auth
from django.contrib import messages
from dateutil import parser
from datetime import datetime

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

# load nlp model
try:
    model_us = pickle.load(open('client/model.sav', 'rb'))
except Exception as e:
    print("Error loading the model:", str(e))

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

    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    users_stories = db.child(f'users/{user_auth}/userstories').get()

    # get the id of user stories, still dictionary need to convert to list
    users_stories_title = db.child(
        f'users/{user_auth}/userstories').shallow().get()
    # convert to list
    print(users_stories_title.val())
    arr_users_stories_title = users_stories_title.val()
    # pengecekan apakah ada id userstories jika tidak ada maka akan tampil dashboard non
    if arr_users_stories_title == None:
        return render(request, 'client-dashboard-non.html', {'user': users_value.val()})
    # jika ada maka akan tampil disini
    else:
        arr_users_stories_title = list(arr_users_stories_title)
        # sort the id
        arr_users_stories_title.sort()

        # get the data for dashboard
        # get the ProjectTitle
        projectTitle = []
        for i in arr_users_stories_title:
            projectTemp = db.child(
                f'users/{user_auth}/userstories/{i}').child('ProjectTitle').get().val()
            projectTitle.append(projectTemp)
        # print(projectTitle)
        # get the user story
        userStories = []
        for i in arr_users_stories_title:
            projectTemp = db.child(
                f'users/{user_auth}/userstories/{i}').child('inputParagraf').get().val()
            userStories.append(projectTemp)
        # print(userStories)

        # get the time stamp
        timestamp = []
        for i in arr_users_stories_title:
            projectTemp = db.child(
                f'users/{user_auth}/userstories/{i}').child('created_at').get().val()
            # projectTemp=projectTemp

            # Parse the timestamp string
            dt_object = parser.parse(projectTemp)

            # Format the date and time components
            formatted_date = dt_object.strftime('%Y-%m-%d')
            formatted_time = dt_object.strftime('%H:%M:%S')

            # Append the formatted date and time to the timestamp list
            timestamp.extend(
                [formatted_date + ' / ' + formatted_time])
        # print(timestamp)
        # for i in arr_users_stories_title:
        #     i=float(i)
        #     projectTemp=datetime.datetime.fromtimestamp(i).strftime('%H-%M %d-%m-%Y')
        #     timestamp.append(projectTemp)
        # print(timestamp)
        # end get data

        # zip the data
        zip_data = zip(arr_users_stories_title,
                       projectTitle, userStories, timestamp)
        UserStory_values = users_stories.val()

        return render(request, 'client-dashboard.html', {'user': users_value.val(), 'UserStory_values': UserStory_values, 'zip_data': zip_data})


# @login_required
def dashboardClientNone(request):
    user = request.user
    return render(request, 'client-dashboard-non.html')


# @login_required
def detailHistory(request, id):
    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    # user.fromJson(users_by_name)

    # get timestamp
    # get the id of user stories, stll dictionary need to convert to list
    users_stories_title = db.child(
        f'users/{user_auth}/userstories').shallow().get()
    # convert to list
    arr_users_stories_title = list(users_stories_title.val())
    # sort the id
    arr_users_stories_title.sort()
    # get the time stamp
    # get the ProjectTitle
    projectTitle = []
    for i in arr_users_stories_title:
        projectTemp = db.child(
            f'users/{user_auth}/userstories/{i}').child('ProjectTitle').get().val()
        projectTitle.append(projectTemp)
    timestamp = []
    for i in arr_users_stories_title:
        projectTemp = db.child(
            f'users/{user_auth}/userstories/{i}').child('created_at').get().val()
        # projectTemp=projectTemp

        # Parse the timestamp string
        dt_object = parser.parse(projectTemp)

        # Format the date and time components
        formatted_date = dt_object.strftime('%Y-%m-%d')
        formatted_time = dt_object.strftime('%H:%M:%S')

        # Append the formatted date and time to the timestamp list
        timestamp.extend(
            [formatted_date + ' / ' + formatted_time])

    return render(request, 'history/history-detail.html', {'user': users_value.val(), 'timestamp': timestamp})


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


def deleteUserStory(request,counter):
    user = request.user
    user_auth = auth.current_user['localId']
     # get the id of user stories, still dictionary need to convert to list
    users_stories_title = db.child(
        f'users/{user_auth}/userstories').shallow().get()
    arr_users_stories_title=list(users_stories_title.val())
    arr_users_stories_title.sort()
    db.child(
        f'users/{user_auth}/userstories').child(arr_users_stories_title[counter-1]).remove()
    return redirect('client:dashboardClient')    


# @login_required
def inputUserStory(request):
    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    # user.fromJson(users_by_name)
    return render(request, 'input-user/input.html', {'user': users_value.val()})


def postInputStory(request):
    import time
    from datetime import datetime, timezone
    import pytz
    ProjectTitle = request.POST.get('ProjectTitle')
    inputParagraf = request.POST.get('inputParagraf')
    # users_value = db.child(f'users/{user_auth}').get()
    idtoken = request.session['uid']
    user_info = auth.get_account_info(idtoken)
    tz = pytz.timezone('Asia/Jakarta')
    created_at = datetime.now(timezone.utc).astimezone(tz).isoformat()
    # Parse the ISO 8601 string into a datetime object
    dt = datetime.fromisoformat(created_at)
    # Convert to a different format (regular date format)
    created_at = dt.strftime("%Y-%m-%d %H:%M:%S")  # Format as desired, e.g., "2023-12-18 10:15:30"
    print(created_at)
    if 'users' in user_info:
        users_list = user_info['users']
        if users_list:
            user_local_id = users_list[0].get('localId')
            print(user_local_id)
            if user_local_id:
                db.child('users').child(user_local_id).child('userstories').push(
                    {"ProjectTitle": ProjectTitle, "inputParagraf": inputParagraf, "created_at": created_at})
                print("Data updated successfully")
                model_us = pickle.load(open('model.sav', 'rb'))
                user_auth = auth.current_user['localId']

                # get the id of user stories, stll dictionary need to convert to list
                users_stories_title = db.child(
                    f'users/{user_auth}/userstories').shallow().get()
                # convert to list
                arr_users_stories_title = list(users_stories_title.val())
                # sort the id
                arr_users_stories_title.sort()
                # model nlp
                lenValue = len(arr_users_stories_title)
                print(arr_users_stories_title)
                ValuePar = db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}').child('inputParagraf').get().val()
                print("value par ", ValuePar)
                print(lenValue)
                outputStory = model_us.nlp_userstory(ValuePar)
                # print(format(outputStory))
                # push database
                db.child('users').child(user_local_id).child('userstories').child(arr_users_stories_title[lenValue-1]).child('outputStory').push(
                    {"outputStory": outputStory})
                # projectTemp=db.child(f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/outputStory').get().val()
                # getting Id for user story
                IdprojectTemp = db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/outputStory').shallow().get()
                print(IdprojectTemp.val())
                IdprojectTemp=IdprojectTemp.val()
                IdprojectTemp = list(IdprojectTemp)
                valueOutput = IdprojectTemp[0]
                print(valueOutput)
                # get output user story
                valueOutput=db.child(f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/outputStory/{valueOutput}').get().val()
                print(valueOutput)
                valueOutput = list(valueOutput.items())
                valueOutput=valueOutput[0][1]
                print(valueOutput)
                # print(valueOutput)
                # valueOutput = valueOutput['outputStory']
                # print(valueOutput)
                # outputStoryIndex = valueOutput[0]
                # print(outputStoryIndex)
                return render(request, 'input-user/output.html', {'valueOutput': valueOutput})


def UpdatePostInputStory(request):
    import time
    from datetime import datetime, timezone
    import pytz
    ProjectTitle = request.POST.get('ProjectTitle')
    inputParagraf = request.POST.get('inputParagraf')
    # users_value = db.child(f'users/{user_auth}').get()
    idtoken = request.session['uid']
    user_info = auth.get_account_info(idtoken)
    tz = pytz.timezone('Asia/Jakarta')
    created_at = datetime.now(timezone.utc).astimezone(tz).isoformat()
    print(created_at)
    if 'users' in user_info:
        users_list = user_info['users']
        if users_list:
            user_local_id = users_list[0].get('localId')
            print(user_local_id)
            if user_local_id:
                # print("Data updated successfully")
                model_us = pickle.load(open('model.sav', 'rb'))
                user_auth = auth.current_user['localId']

                # get the id of user stories, stll dictionary need to convert to list
                users_stories_title = db.child(
                    f'users/{user_auth}/userstories').shallow().get()
                # convert to list
                arr_users_stories_title = list(users_stories_title.val())
                # sort the id
                arr_users_stories_title.sort()
                # model nlp
                lenValue = len(arr_users_stories_title)
                print(arr_users_stories_title)
                db.child('users').child(user_local_id).child('userstories').child(arr_users_stories_title[lenValue-1]).update(
                    {"ProjectTitle": ProjectTitle, "inputParagraf": inputParagraf, "created_at": created_at})
                ValuePar = db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}').child('inputParagraf').get().val()
                print("value par ", ValuePar)
                print(lenValue)
                outputStory = model_us.nlp_userstory(ValuePar)
                # print(format(outputStory))
                # projectTemp=db.child(f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/outputStory').get().val()
                # getting Id for user story
                IdprojectTemp = db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/outputStory').shallow().get()
                print(IdprojectTemp.val())
                IdprojectTemp=IdprojectTemp.val()
                IdprojectTemp = list(IdprojectTemp)
                IdprojectTemp.sort()
                print(IdprojectTemp)
                # push database
                db.child('users').child(user_local_id).child('userstories').child(arr_users_stories_title[lenValue-1]).child('outputStory').child(IdprojectTemp[0]).set(
                    {"outputStory": outputStory})
                IdprojectTemp = db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/outputStory').shallow().get()
                print(IdprojectTemp.val())
                IdprojectTemp=IdprojectTemp.val()
                IdprojectTemp = list(IdprojectTemp)
                valueOutput = IdprojectTemp[0]
                print(valueOutput)
                # get output user story
                valueOutput=db.child(f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/outputStory/{valueOutput}').get().val()
                print(valueOutput)
                valueOutput = list(valueOutput.items())
                valueOutput=valueOutput[0][1]
                print(valueOutput)
                
                # UpdateValueOutput = IdprojectTemp[(len(IdprojectTemp)-3)]
                # print(UpdateValueOutput)
                # get output user story
                # UpdateValueOutput=db.child(f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/{UpdateValueOutput}').get().val()
                # print(UpdateValueOutput)
                # UpdateValueOutput = list(UpdateValueOutput.items())
                # UpdateValueOutput=UpdateValueOutput[0][1]
                # print(UpdateValueOutput)
                # print(valueOutput)
                # valueOutput = valueOutput['outputStory']
                # print(valueOutput)
                # outputStoryIndex = valueOutput[0]
                # print(outputStoryIndex)
                return render(request, 'input-user/output.html', {'valueOutput':valueOutput})


def inputScenario(request, counter):
    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    ScenarioTitle = request.POST.get('ScenarioTitle')
    inputParagraf = request.POST.get('inputParagraf')

    import time
    from datetime import datetime, timezone
    import pytz
    # ProjectTitle = request.POST.get('ProjectTitle')
    # inputParagraf = request.POST.get('inputParagraf')
    # users_value = db.child(f'users/{user_auth}').get()
    idtoken = request.session['uid']
    user_info = auth.get_account_info(idtoken)
    tz = pytz.timezone('Asia/Jakarta')
    created_at = datetime.now(timezone.utc).astimezone(tz).isoformat()
    print(created_at)
    if 'users' in user_info:
        users_list = user_info['users']
        if users_list:
            user_local_id = users_list[0].get('localId')
            print(user_local_id)
            if user_local_id:
                # db.child('users').child(user_local_id).child('userstories').push(
                #     {"inputParagraf": inputParagraf,"created_at":created_at})
                # print("Data updated successfully")
                # model_us = pickle.load(open('modelScenario.sav', 'rb'))
                user_auth = auth.current_user['localId']

                # get the id of user stories, stll dictionary need to convert to list
                users_stories_title = db.child(
                    f'users/{user_auth}/userstories').shallow().get()
                # convert to list
                arr_users_stories_title = list(users_stories_title.val())
                # sort the id
                arr_users_stories_title.sort()
                # model nlp
                lenValue = len(arr_users_stories_title)
                print(arr_users_stories_title)
                # get user stories tittle
                ValueTitle = db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}').child('ProjectTitle').get().val()
                print("value title ", ValueTitle)
                ValuePar = db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}').child('inputParagraf').get().val()
                print("value par ", ValuePar)
                print(lenValue)
                
                # getting Id for user story
                IdprojectTemp = db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/outputStory').shallow().get()
                print(IdprojectTemp.val())
                IdprojectTemp=IdprojectTemp.val()
                IdprojectTemp = list(IdprojectTemp)
                valueOutput = IdprojectTemp[0]
                print(valueOutput)
                # get output user story
                valueOutput=db.child(f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/outputStory/{valueOutput}').get().val()
                print(valueOutput)
                valueOutput = list(valueOutput.items())
                valueOutput=valueOutput[0][1]
                outputStoryIndex=valueOutput[counter]
                print(valueOutput)
    return render(request, 'output-user-scenario/input_scenario.html', {'user': users_value.val(), 'outputStoryIndex': outputStoryIndex, 'counter': counter, 'title': ValueTitle})


def outputScenario(request, counter):
    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()

    import time
    from datetime import datetime, timezone
    import pytz
    # ProjectTitle = request.POST.get('ProjectTitle')
    ScenarioTitle = request.POST.get('ScenarioTitle')
    inputParagraf = request.POST.get('inputParagraf')
    # users_value = db.child(f'users/{user_auth}').get()
    idtoken = request.session['uid']
    user_info = auth.get_account_info(idtoken)
    tz = pytz.timezone('Asia/Jakarta')
    created_at = datetime.now(timezone.utc).astimezone(tz).isoformat()
    print(created_at)
    if 'users' in user_info:
        users_list = user_info['users']
        if users_list:
            user_local_id = users_list[0].get('localId')
            print(user_local_id)
            if user_local_id:
                # db.child('users').child(user_local_id).child('userstories').push(
                #     {"inputParagraf": inputParagraf,"created_at":created_at})
                # print("Data updated successfully")
                model_us = pickle.load(open('modelScenario.sav', 'rb'))
                user_auth = auth.current_user['localId']

                # get the id of user stories, stll dictionary need to convert to list
                users_stories_title = db.child(
                    f'users/{user_auth}/userstories').shallow().get()
                # convert to list
                arr_users_stories_title = list(users_stories_title.val())
                # sort the id
                arr_users_stories_title.sort()
                # model nlp
                lenValue = len(arr_users_stories_title)
                print(arr_users_stories_title)
                # get user stories tittle
                ValueTitle = db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}').child('ProjectTitle').get().val()
                print("value title ", ValueTitle)
                ValuePar = db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}').child('inputParagraf').get().val()
                print("value par ", ValuePar)
                print(lenValue)
                # getting Id for user story
                IdprojectTemp = db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/outputStory').shallow().get()
                print(IdprojectTemp.val())
                IdprojectTemp=IdprojectTemp.val()
                IdprojectTemp = list(IdprojectTemp)
                valueOutput = IdprojectTemp[0]
                print(valueOutput)
                # get output user story
                valueOutput=db.child(f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/outputStory/{valueOutput}').get().val()
                print(valueOutput)
                valueOutput = list(valueOutput.items())
                valueOutput=valueOutput[0][1]
                outputStoryIndex=valueOutput[counter]
                print(valueOutput)
                # who=outputStoryIndex['who'][0]
                # what=outputStoryIndex['what'][0]
                # why=outputStoryIndex['why'][0]
                # print(outputStoryIndex)
                # hasilOutputStory=[]
                # hasilOutputStory.extend([who, what, why])
                # print(hasilOutputStory)
                db.child('users').child(user_local_id).child('userstories').child(arr_users_stories_title[lenValue-1]).child('userStoryScenario').push(
                    {"ScenarioTitlte": ScenarioTitle, "inputParagraf": inputParagraf})
                # print(format(outputStory))
                
                keyvalueUSS=db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/userStoryScenario').get().val()
               
                keyvalueUSS=list(keyvalueUSS)
                print('keyvalueUSS',keyvalueUSS)
                len_keyvalueUSS=len(keyvalueUSS)
                valueUss=db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/userStoryScenario/{keyvalueUSS[len_keyvalueUSS-1]}').get().val()
                print(valueUss)
                valueUss = list(valueUss.items())
                valueUss = valueUss[1][1]
                print(valueUss)
                outputUSScenario = model_us.nlp_UserStoryScenario(valueUss)
                print('output', outputUSScenario)
                # push database
                db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/userStoryScenario/{keyvalueUSS[len_keyvalueUSS-1]}').child('outputUSScenario').push({'outputUSScenario': outputUSScenario})
                retrieveUSS=db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/userStoryScenario/{keyvalueUSS[len_keyvalueUSS-1]}').child('outputUSScenario').shallow().get()
                print(retrieveUSS.val())
                retrieveUSSKey=list(retrieveUSS.val())
                # # ScenarioTitle=retrieveUSSKey[1]
                # # print(ScenarioTitle)
                retrieveUSSKey=retrieveUSSKey[0]
                retrieveUSS=db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/userStoryScenario/{keyvalueUSS[len_keyvalueUSS-1]}').child('outputUSScenario').child(retrieveUSSKey).get().val()
                print(retrieveUSS)
                # retrieveUSS=db.child(
                #     f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/userStoryScenario/{retrieveUSSKey}').get().val()
                # print(retrieveUSS)
                retrieveUSS=list(retrieveUSS.items())
                retrieveUSS=retrieveUSS[0][1]
                print(retrieveUSS)
                
                # print('tes',retrieveUSS)
                # testing

    return render(request, 'output-user-scenario/output_scenario.html', {'user': users_value.val(), 'outputStoryIndex': outputStoryIndex, 'counter': counter,'retrieveUSS': retrieveUSS, 'title':ValueTitle})


def UpdateOutputScenario(request, counter):
    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()

    import time
    from datetime import datetime, timezone
    import pytz
    # ProjectTitle = request.POST.get('ProjectTitle')
    ScenarioTitle = request.POST.get('ScenarioTitle')
    inputParagraf = request.POST.get('inputParagraf')
    # users_value = db.child(f'users/{user_auth}').get()
    idtoken = request.session['uid']
    user_info = auth.get_account_info(idtoken)
    tz = pytz.timezone('Asia/Jakarta')
    created_at = datetime.now(timezone.utc).astimezone(tz).isoformat()
    print(created_at)
    if 'users' in user_info:
        users_list = user_info['users']
        if users_list:
            user_local_id = users_list[0].get('localId')
            print(user_local_id)
            if user_local_id:
                # db.child('users').child(user_local_id).child('userstories').push(
                #     {"inputParagraf": inputParagraf,"created_at":created_at})
                # print("Data updated successfully")
                model_us = pickle.load(open('modelScenario.sav', 'rb'))
                user_auth = auth.current_user['localId']

                # get the id of user stories, stll dictionary need to convert to list
                users_stories_title = db.child(
                    f'users/{user_auth}/userstories').shallow().get()
                # convert to list
                arr_users_stories_title = list(users_stories_title.val())
                # sort the id
                arr_users_stories_title.sort()
                # model nlp
                lenValue = len(arr_users_stories_title)
                print(arr_users_stories_title)
                ValuePar = db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}').child('inputParagraf').get().val()
                print("value par ", ValuePar)
                print(lenValue)
                # getting Id for user story
                IdprojectTemp = db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/outputStory').shallow().get()
                print(IdprojectTemp.val())
                IdprojectTemp=IdprojectTemp.val()
                IdprojectTemp = list(IdprojectTemp)
                valueOutput = IdprojectTemp[0]
                print(valueOutput)
                # get output user story
                valueOutput=db.child(f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/outputStory/{valueOutput}').get().val()
                print(valueOutput)
                valueOutput = list(valueOutput.items())
                valueOutput=valueOutput[0][1]
                outputStoryIndex=valueOutput[counter]
                print(valueOutput)
                # who=outputStoryIndex['who'][0]
                # what=outputStoryIndex['what'][0]
                # why=outputStoryIndex['why'][0]
                # print(outputStoryIndex)
                # hasilOutputStory=[]
                # hasilOutputStory.extend([who, what, why])
                # print(hasilOutputStory)

                # get id user story scenario
                IdUSScenario=db.child('users').child(user_local_id).child('userstories').child(arr_users_stories_title[lenValue-1]).child('userStoryScenario').shallow().get()
                print(IdUSScenario.val())
                IdUSScenario=list(IdUSScenario.val())
                len_IdUSScenario=len(IdUSScenario)
                # update data project title n input paragraf
                db.child('users').child(user_local_id).child('userstories').child(arr_users_stories_title[lenValue-1]).child('userStoryScenario').child(IdUSScenario[len_IdUSScenario-1]).update(
                    {"ScenarioTitlte": ScenarioTitle, "inputParagraf": inputParagraf})
                
                # retreive data for processing in model
                valueUss=db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/userStoryScenario/{IdUSScenario[len_IdUSScenario-1]}/inputParagraf').get().val()
                print("valueUss",valueUss)


                # processing in model
                outputUSScenario = model_us.nlp_UserStoryScenario(valueUss)
                print(outputUSScenario)

                # get the id of output user stories scenario, stll dictionary need to convert to list
                keyvalueOutputUSS=db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/userStoryScenario/{IdUSScenario[0]}/outputUSScenario').shallow().get()
                print(keyvalueOutputUSS.val())
               
                keyvalueOutputUSS=list(keyvalueOutputUSS.val())
                len_keyvalueOutputUSS=len(keyvalueOutputUSS)
                keyvalueOutputUSS=keyvalueOutputUSS[len_keyvalueOutputUSS-1]
                print('keyvalueOutputUSS',keyvalueOutputUSS)
                
                # update data output US scenario
                db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/userStoryScenario/{IdUSScenario[len_IdUSScenario-1]}/outputUSScenario/{keyvalueOutputUSS}').update({'outputUSScenario': outputUSScenario})
                # print(valueUss)
                # valueUss=list(valueUss.items())
                # valueUss=valueUss[1][1]
                # print(valueUss)
                # print('output',outputUSScenario)
                # # push database
                # db.child(
                #     f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/userStoryScenario/{keyvalueUSS[len_keyvalueUSS-1]}').push({'outputUSScenario': outputUSScenario})

                # retreive data for output user story scenario
                retrieved_data= db.child(
                    f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/userStoryScenario/{IdUSScenario[len_IdUSScenario-1]}/outputUSScenario/{keyvalueOutputUSS}/outputUSScenario').get().val()
                print(retrieved_data)
                # print(retrieveUSS.val())
                # retrieveUSSKey=list(retrieveUSS.val())
                # # ScenarioTitle=retrieveUSSKey[1]
                # # print(ScenarioTitle)
                # retrieveUSSKey=retrieveUSSKey[0]
                # retrieveUSS=db.child(
                #     f'users/{user_auth}/userstories/{arr_users_stories_title[lenValue-1]}/userStoryScenario/{retrieveUSSKey}').get().val()
                # print(retrieveUSS)
                # retrieveUSS=list(retrieveUSS.items())
                # retrieveUSS=retrieveUSS[0][1]
                # retrieved_data = retrieveUSS['outputUSScenario']
                # print(retrieved_data)
                # # print('tes',retrieveUSS)
                # # testing

    return render(request, 'output-user-scenario/output_scenario.html', {'user': users_value.val(), 'outputStoryIndex': outputStoryIndex, 'counter': counter,'retrieveUSS': retrieved_data})


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
    # get the id of user stories, still dictionary need to convert to list
    users_stories_title = db.child(
        f'users/{user_auth}/userstories').shallow().get()
    if users_stories_title.val() is None:
        project_complished=0
        return render(request, 'user_profile/user-profile.html', {'user': users_value.val(),'project_complished':project_complished})
    # convert to list
    arr_users_stories_title = list(users_stories_title.val())
    project_complished=len(arr_users_stories_title)
    return render(request, 'user_profile/user-profile.html', {'user': users_value.val(),'project_complished':project_complished})


def editProfile(request):
    user = request.user
    user_auth = auth.current_user['localId']
    users_value = db.child(f'users/{user_auth}').get()
    # user.fromJson(users_by_name)
    return render(request, 'user_profile/edit-profile.html', {'user': users_value.val()})


def posteditprofile(request):
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
