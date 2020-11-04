from django.shortcuts import render
from django.http import HttpResponse

def viewTrainersView(request) :
    return HttpResponse('View Your Trainers!')

# Create your views here.