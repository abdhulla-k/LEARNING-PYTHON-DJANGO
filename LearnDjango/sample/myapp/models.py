from django.db import models

# Create your models here.

class Features:   # It is a model. It connected to views.py
    id = int
    name = str
    details = str
    is_currect = bool
