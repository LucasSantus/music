from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import json

def index(request):

    api_request = requests.get("http://127.0.0.1:8000/api/list/?search=")
    list_musicas = json.loads(api_request.text)
    
    if request.POST:
        pesquisa = request.POST.get("pesquisa", None)
                            
        api_request = None
        list_musicas = None

        api_request = requests.get("http://127.0.0.1:8000/api/list/?search="+pesquisa)
        list_musicas = json.loads(api_request.text)

        if not list_musicas: 
            api_request = requests.get("http://127.0.0.1:8000/api/music/?format=json")
            list_musicas = json.loads(api_request.text)

            messages.error(request, "Música não encontrada!")

    context = {
        "list_musicas": list_musicas,
    }
    return render(request, "musica/index.html", context)