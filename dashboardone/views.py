from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"dashboardone/home.html")

def analytics(request):
    return render(request,"dashboardone/analytics.html")

def reports(request):
    return render(request, "dashboardone/reports.html")