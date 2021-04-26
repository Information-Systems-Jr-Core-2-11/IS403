from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon

# Create your views here.
def pokedexPageView(request):
    # return render(request, './template/index.html')
    context = {'Pokedex' : Pokemon.objects.all()}
    return render(request, 'ViewPokedex/index.html', context)
