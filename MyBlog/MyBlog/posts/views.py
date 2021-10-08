from django.shortcuts import render

# Create your views here.

def index(request):                            # create the function like this. then create a directory and then create the html file. go to that html file 
    return render(request, 'index.html')
