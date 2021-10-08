from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):                            # create the function like this. then create a directory and then create the html file. go to that html file 
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def post(request, pk):
    posts = Post.objects.get(id = pk)
    return render(request, 'post.html', {'posts': posts})
