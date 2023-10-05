from django.shortcuts import render
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'base.html')

def user(request):
    return render(request, 'user.html')
