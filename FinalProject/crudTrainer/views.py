from django.shortcuts import render
from django.http import HttpResponse

def crudTrainerPageView(request) :
    return HttpResponse('crudTrainer')

def createTrainerPageView(request) :
    return render(request, 'createTrainer/create.html')

def updateTrainerPageView(request) :
    return render(request, 'updateTrainer/update.html')

def deleteTrainerPageView(request) :
    return render(request, 'deleteTrainer/delete.html')

