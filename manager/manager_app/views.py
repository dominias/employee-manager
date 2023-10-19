from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def testFunc(request):
    return HttpResponse("Manager App")