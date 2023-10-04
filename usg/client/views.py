from django.shortcuts import render

# Create your views here.
def detailHistory(request):
    return render(request, 'history/history-detail.html')