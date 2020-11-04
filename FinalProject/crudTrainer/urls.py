from django.urls import path
from .views import crudTrainerPageView

urlpatterns = [
    path("crudTrainer/", crudTrainerPageView, name="crudTrainer"),
]