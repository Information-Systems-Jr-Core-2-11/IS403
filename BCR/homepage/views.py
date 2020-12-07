from django.shortcuts import render

# Create your views here.

def homePageView(request):
    return render(request, 'homepage/index.html')

def ourMissionPageView(request):
    return render(request, 'homepage/ourmission.html')

def loginPageView(request):
    return render(request, 'homepage/login.html')

def signupPageView(request):
    return render(request, "homepage/signupmain.html")

def signupEmployerPageView(request):
    return render(request, 'homepage/signupemployer.html')

def signupApplicantPageView(request):
    return render(request, 'homepage/signupapplicant.html')