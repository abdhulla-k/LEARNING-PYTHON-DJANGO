from django.urls import path
from . import views         # first import path and views for configer urls

urlpatterns = [
    path('', views.index, name = 'index')   # create new url. then go to the views.py and create the function 
]