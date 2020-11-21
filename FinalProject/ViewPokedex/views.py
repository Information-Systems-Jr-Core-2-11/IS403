from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pokedexPageView(request):
    # return render(request, './template/index.html')
    return render(request, 'ViewPokedex/index.html')
