from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Todo;

def homeview(request):
    data = Todo.objects.all()
    return render(
        request,
        'home/home.html',
        context={"data":data }
    )