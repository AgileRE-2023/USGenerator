from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')
def projectView(request):
    return render(request, 'project-view.html')