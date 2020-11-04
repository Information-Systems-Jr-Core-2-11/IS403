from django.shortcuts import render
from django.http import HttResponse

def crudTrainerPageView(request) :
    return HttpResponse('crudTrainer')

def createTrainerPageView(request) :
    return HttpResponse('create trainer')

def readTrainerPageView(request) :
    return HttpResponse('read trainer')

def updateTrainerPageView(request) :
    return HttpResponse('update trainer')

def deleteTrainerPageView(request) :
    return HttpResponse('delete trainer')
