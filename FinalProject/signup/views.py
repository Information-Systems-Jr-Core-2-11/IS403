from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signupPageView(request):
    return HttpResponse('sign up')

def signedupPageView(request):
    return HttpResponse('signed up')