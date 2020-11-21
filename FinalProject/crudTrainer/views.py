from django.shortcuts import render
from django.http import HttpResponse

def crudTrainerPageView(request) :
    return HttpResponse('crudTrainer')

def createTrainerPageView(request) :
    return render(request, 'CRUD_Trainer/create.html')

def updateTrainerPageView(request) :
    return render(request, 'CRUD_Trainer/update.html')

def deleteTrainerPageView(request) :
    return render(request, 'CRUD_Trainer/delete.html')

