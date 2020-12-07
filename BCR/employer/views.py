from django.shortcuts import render

# Create your views here.
def employerPageView(request):
    return render(request, 'employer/index.html')

def findApplicantsPageView(request):
    return render(request, 'employer/findapplicants.html')

def applicantProfilePageView(request):
    return render(request, 'employer/applicantprofile.html')

def postJobPageView(request):
    return render(request, 'employer/postjob.html')