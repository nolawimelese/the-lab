from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length = 20)
    description = models.TextField(default = "Enter Here...", max_length = 200)
    minutes = models.IntegerField(default = 0)
    completed = models.BooleanField(default = False)