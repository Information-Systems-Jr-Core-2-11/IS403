from django.urls import path
from .views import crudTrainerPageView, createTrainerPageView, updateTrainerPageView, deleteTrainerPageView

urlpatterns = [
    path("crudTrainer/", crudTrainerPageView, name="crudTrainer"),
    path("createTrainer/", createTrainerPageView, name="createTrainer"),
    path("updateTrainer/", updateTrainerPageView, name="updateTrainer"),
    path("deleteTrainer/", deleteTrainerPageView, name="deleteTrainer"),
]