from django.shortcuts import render
from django.http import HttpResponse

def dashboard_view(request):
    return render(request, 'dashboard/dashboard_view.html')
