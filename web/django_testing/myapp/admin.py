from django.contrib import admin

# importing our todo model from models.py
from .models import TodoItem
# Register your models here.

admin.site.register(TodoItem)