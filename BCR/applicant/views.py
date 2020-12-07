from django.shortcuts import render

# Create your views here.

def applicantPageView(request):
    return render(request, 'applicant/index.html')

def findAJobPageView(request):
    return render(request, 'applicant/findajob.html')

def jobListingsPageView(request):
    return render(request, 'applicant/joblistings.html')

def jobDetailsPageView(request):
    return render(request, 'applicant/jobdetails.html')

def companyProfilePageView(request):
    return render(request, 'applicant/companyprofile.html')

def skillRecommenderPageView(request):
    return render(request, 'applicant/skillrecommender.html')
