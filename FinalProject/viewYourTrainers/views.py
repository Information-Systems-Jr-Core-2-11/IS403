from django.shortcuts import render
from django.http import HttpResponse

def viewTrainersView(request) :
    return render(request, 'viewYourTrainers/trainers.html')

# Create your views here.