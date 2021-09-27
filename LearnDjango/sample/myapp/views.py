from django.shortcuts import render
from django.http import HttpResponse
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
   feature1 = Features()
   feature1.id = 0
   feature1.name = 'Fast'
   feature1.details = 'Our service is very quick'
   feature1.is_currect = True

   feature2 = Features()
   feature2.id = 0
   feature2.name = 'Reliable'
   feature2.details = 'Our service is Reliable'
   feature2.is_currect = True

   feature3 = Features()
   feature3.id = 0
   feature3.name = 'Easy to use'
   feature3.details = 'Our service is very Easy to use'
   feature3.details = False

   feature4 = Features()
   feature4.id = 0
   feature4.name = 'Affordable'
   feature4.details = 'Our service is affordable for everyone'
   feature4.is_currect = False

   features = [feature1, feature2, feature3, feature4] # to be dynamic

   return render(request, 'index.html',{'features':features})


def counter(request):
   text = request.POST['text']  # learned about GET and POST methods. POST is more safe
   amount_of_words = len(text.split())
   return render(request, 'counter.html', {'amount': amount_of_words}) # go and create the html file