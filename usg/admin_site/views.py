from django.shortcuts import render
from django.template import loader

# Create your views here.
config = {
    'apiKey': "AIzaSyA0vBvWec1huC34E048rzWtUwkKd5bfAxU",
    'authDomain': "usg-django-pplprak.firebaseapp.com",
    'databaseURL': "https://usg-django-pplprak-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "usg-django-pplprak",
    'storageBucket': "usg-django-pplprak.appspot.com",
    'messagingSenderId': "1048754184838",
    'appId': "1:1048754184838:web:16794aa3970c3b8dd2a707",
    'measurementId': "G-PC679TGGMD"
}
firebase = pyrebase.initializeApp(config)
auth = firebase.auth()
db = firebase.database()


def signin(request):
    return render(request, 'signin.html')


def postsignin(request):
    email=request.POST.get('email')
    password=request.POST.get('password')

    user = auth.sign_in_with_email_and_password(email,password)

    return render(request, "welcome.html", {"email":email})


def baseAdmin(request):
    return render(request, 'base-admin.html')


def user(request):
    return render(request, 'user.html')


def projectView(request):
    return render(request, 'project-view.html')


def dashboard(request):
    return render(request, 'dashboard.html')
