from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


data={"name":"django app", "value":20}

fruits = ['apple', 'Banana', 'Cherry', 'Orange','Banana']

class_value={"text"}

firstof_test = {
'val1': '',
'val2': '',
'val3': 'Hello, World!'
}


def homeview(request):
    return render(
        request,
        'home.html',
        context={
            "data":data ,
            "fruits":fruits,
            "class_value":class_value,
            "firstof_test":firstof_test
        }
    )