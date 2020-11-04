from django.urls import path
from .views import viewTrainersView

urlpatterns = [
    path('viewTrainers/', viewTrainersView, name = 'viewTrainer')
]