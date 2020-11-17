from django.urls import path
from .views import pokedexPageView
from .views import pokemonPageView

urlpatterns = [
    path('', pokedexPageView, name='pokedex'),
    path('<str:pokemon>/', pokemonPageView, name='pokemon_name'),
]
