from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hey, Welcome</h1>') 

# go to main projuct and add this app (myapp) to urls.py of the main project
