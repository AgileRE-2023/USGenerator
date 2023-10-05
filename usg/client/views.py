from django.shortcuts import render

# Create your views here.
def outputScenario(request):
    return render(request, 'output-user-scenario/output_scenario.html')