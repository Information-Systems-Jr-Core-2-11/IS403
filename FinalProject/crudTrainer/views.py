from django.shortcuts import render
from django.http import HttResponse

def indexPageView(request) :
    return HttpResponse('crudTrainer')
