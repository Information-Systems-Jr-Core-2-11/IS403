from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon, Trainer

def crudTrainerPageView(request) :
    return HttpResponse('crudTrainer')

def createTrainerPageView(request) :

    context = {"Trainers": Trainer.objects.all()}
    
    return render(request, 'CRUD_Trainer/create.html', context)

def updateTrainerPageView(request) :


    if request.method == 'POST':
        update_trainer = Trainer.objects.filter(id = request.POST['trainer_id_update'])
        context = {'update_trainer' : update_trainer}
        return render(request, 'CRUD_Trainer/updateform.html', context)

    context = {"Trainers": Trainer.objects.all()}

    return render(request, 'CRUD_Trainer/update.html', context)

def updateTrainerRecord(request) :
    print(request.POST.get('trainer_id'))
    trainerToUpdate = Trainer.objects.get(id = request.POST.get('trainer_id'))
    trainerToUpdate.first_name = request.POST.get('trainer_first_name')
    trainerToUpdate.last_name = request.POST.get('trainer_last_name')
    trainerToUpdate.home_town = request.POST.get('hometown')
    trainerToUpdate.gender = request.POST.get('gender')
    trainerToUpdate.fav_type = request.POST.get('favtype')

    trainerToUpdate.save()

    context = {"Trainers": Trainer.objects.all()}
    return render(request, 'viewYourTrainers/trainers.html', context)

def deleteTrainerPageView(request) :

    if request.method == 'POST':
        deleted_trainer = Trainer.objects.filter(id = request.POST['trainer_id_delete']).delete()
        context = {"Trainers": Trainer.objects.all()}
        return render(request, 'viewYourTrainers/trainers.html', context)

    context = {"Trainers": Trainer.objects.all()}
    return render(request, 'CRUD_Trainer/delete.html', context)

