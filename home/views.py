from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homeview(request):
    return HttpResponse("Hello, world. You're at the index page.")