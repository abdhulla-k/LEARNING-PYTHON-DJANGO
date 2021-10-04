from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Features

# Create your views here.
#def index(request):
   # return HttpResponse('<h1>Hey, Welcome</h1>') 

# go to main projuct and add this app (myapp) to urls.py of the main project

# how to add external data or add data from 'templates'
#def index(request):
   # return render(request, 'index.html')


# how to send dinamic data .the data may coming from data base
#def index(request):
#   name = 'Patric'
#   return render(request, 'index.html',{'name':name})
#   # go to the templates file and add the key

# add more data. just like above
def index(request):
   content ={
      'name' : 'Abdhu',
      'age' : 20,
      'place' : 'Kerala',
      'nationality' : 'India'
   }
   #feature1 = Features()
   #feature1.id = 0
   #feature1.name = 'Fast'
   #feature1.details = 'Our service is very quick'
   #feature1.is_currect = True

   #feature2 = Features()
   #feature2.id = 0
   #feature2.name = 'Reliable'
   #feature2.details = 'Our service is Reliable'
   #feature2.is_currect = True

   #feature3 = Features()
   #feature3.id = 0
   #feature3.name = 'Easy to use'
   #feature3.details = 'Our service is very Easy to use'
   #feature3.details = False

   #feature4 = Features()
   #feature4.id = 0
   #feature4.name = 'Affordable'
   #feature4.details = 'Our service is affordable for everyone'
   #feature4.is_currect = False

   #features = [feature1, feature2, feature3, feature4] # to be dynamic
   features = Features.objects.all()   # it is coming from data base.

   return render(request, 'index.html',{'features':features})

def register(request):
   if request.method == 'POST':
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      password2 = request.POST['password2']

      if password == password2:
         # import redirect
         # from django.contrib.auth.models import user, auth
         # from django.contrib import messages
         if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Used')
            return redirect('register')
         elif User.objects.filter(username = username):
            messages.info(request, 'Username already used')
            return redirect('register')
         else:
            user = User.objects.create_user(username = username, email = email, password = password)
            user.save()
            return redirect('login')
      else:
         messages.info(request, 'Password Not The Same')
         return redirect('register')
   else:
      return render(request, 'register.html')

def Login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']

      user = auth.authenticate(username = username, password = password)
      if user is not None:
         auth.login(request, user)
         return redirect('/')
      else:
         messages.info(request, 'Credentials invalid')
         return render('login')
   else:
      return render(request, 'login.html')


   

def counter(request):
   text = request.POST['text']  # learned about GET and POST methods. POST is more safe
   amount_of_words = len(text.split())
   return render(request, 'counter.html', {'amount': amount_of_words}) # go and create the html file