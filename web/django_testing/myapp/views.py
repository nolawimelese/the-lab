from django.shortcuts import render
from django.http import HttpResponse

from .models import TodoItem
# Create your views here.


def home(request):
    """
    request: accesses query parameters and body of requests
    """ 
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})