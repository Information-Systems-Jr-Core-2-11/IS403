from django.shortcuts import render

# Create your views here.
def employerPageView(request):
    return render(request, 'employer/index.html')