from django.shortcuts import render
from Constants.constants import Server

# Create your views here.
def LoginPage(request):
    return render(request , 'Auth/login.html')

def RegisterPage(request):
    return render(request , 'Auth/register.html')

def HomePage(request):
    # url = Server() + 'API/AuthGet'
    # response = request.GET.get(url)
    return render(request , 'Auth/home.html' , {'Response': 'response'})