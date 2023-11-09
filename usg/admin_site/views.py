from django.shortcuts import render
from django.template import loader

def baseAdmin(request):
    return render(request, 'base-admin.html')


def user(request):
    return render(request, 'user.html')


def projectView(request):
    return render(request, 'project-view.html')


def dashboard(request):
    return render(request, 'dashboard.html')
