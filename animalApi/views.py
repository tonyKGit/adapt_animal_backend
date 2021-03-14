from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testApi(request):
    if request == 'GET' :
        return "get success"
    else:
        return "false"

def mainPage(request):
    return HttpResponse("test")