from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pokedexPageView(request):
    context = {
        "name" : "jonah",
        "movies" : ["Star wars", "Three Amigos", "Elf"]
    }
    # return render(request, './template/index.html')
    return render(request, 'ViewPokedex/index.html', context)