from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon, Trainer


def viewTrainersView(request) :

    if request.method == 'POST':
        #Create a new employee object from the Employee model
        new_trainer = Trainer()
        #grab the data from the form and store it to the new object
        new_trainer.first_name = request.POST.get('trainer_first_name')
        new_trainer.last_name = request.POST.get('trainer_last_name')
        new_trainer.home_town = request.POST.get('hometown')
        new_trainer.gender = request.POST.get('gender')
        new_trainer.fav_type = request.POST.get('favtype')
        #store the record form the model to the table
        new_trainer.save()

    context = {'Trainers' : Trainer.objects.all()}
    return render(request, 'viewYourTrainers/trainers.html', context)

# Create your views here.