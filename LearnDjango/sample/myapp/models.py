from django.db import models

# Create your models here.

class Features(models.Model):   # It is a model. It connected to views.py
    #id = int
    name = models.CharField(max_length= 100)
    details = models.CharField(max_length= 500)
    #is_currect = bool
