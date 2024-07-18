from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


data={
    "name":"django app",
    "value":20

}

def homeview(request):
    return render(request,'home.html' ,context=data )