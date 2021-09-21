from django.shortcuts import render
from django.http import HttpResponse

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
   return render(request, 'index.html', content)

def counter(request):
   text = request.GET['text']
   amount_of_words = len(text.split())
   return render(request, 'counter.html', {'amount': amount_of_words}) # go and create the html file