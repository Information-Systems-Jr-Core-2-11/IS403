from django.urls import path
from .views import pokedexPageView

urlpatterns = [
    path('', pokedexPageView, name='pokedex'),
]
