from django.urls import path
from .views import pokedexPageView

urlpatterns = [
    path('pokedex/', pokedexPageView, name='pokedex'),
]
