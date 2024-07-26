from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def loginview(request):
    return render(
        request,
        'login/login.html',
        # context={
        #     "data":data ,
        #     "fruits":fruits,
        #     "class_value":class_value,
        #     "firstof_test":firstof_test
        # }
    )