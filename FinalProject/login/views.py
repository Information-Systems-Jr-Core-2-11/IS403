from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loginPageView(request):
    return HttpResponse('login')

def loggedinPageView(request):
    return HttpResponse('logged in')