from django.contrib import admin
from django.db import models
from .models import Room, Message

# Register your models here.

admin.site.register(Room)
admin.site.register(Message)