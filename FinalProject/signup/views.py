from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signupPageView(request):
    return render(request, 'Signup/signup.html')

def signedupPageView(request):
    return HttpResponse('signed up')