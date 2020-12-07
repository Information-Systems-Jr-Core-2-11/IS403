from django.shortcuts import render

# Create your views here.

def applicantPageView(request):
    return render(request, 'applicant/index.html')

def findAJobPageView(request):
    return render(request, 'applicant/findajob.html')