from django.shortcuts import render

# Create your views here.
def detailHistory(request):
    return render(request, 'history/history-detail.html')
def base(request):
    return render(request,'base.html')
def baseSignIn(request):
    return render(request,'base_signin.html')
def SignIn(request):
    return render(request,'signin-reg/signin.html')
def regist(request):
    return render(request,'signin-reg/regist.html')
