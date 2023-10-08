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
def outputScenario(request):
    return render(request, 'output-user-scenario/output_scenario.html')
def inputUserStory(request):
    return render(request, 'input-user/input.html')
def history(request):
    return render(request, 'history/history.html')
def userProfile(request):
    return render(request, 'user_profile/user-profile.html')

