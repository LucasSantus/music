from django.shortcuts import render, redirect
import requests
import json

def index(request):
    try:
    
        if request.POST:
            pesquisa = request.POST.get("pesquisa", None)
            api_request = requests.get("http://127.0.0.1:8000/api/list/?search="+pesquisa)
            list_musicas = json.loads(api_request.text)
        
        else:
            api_request = requests.get("http://127.0.0.1:8000/api/music/?format=json")
            list_musicas = json.loads(api_request.text)

    except:
        list_musicas = None

    context = {
        "list_musicas": list_musicas,
    }
    return render(request, "musica/index.html", context)