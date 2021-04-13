from django.shortcuts import render, redirect
import requests
import json

def index(request):

    buscar_dados()

    try:
        api_request = requests.get("http://127.0.0.1:8000/api/music/?format=json")
        list_musica = json.loads(api_request.text)
    except:
        list_musica = "Não Possui Músicas"

    context = {
        "list_musicas": list_musica,
    }

    return render(request, "musica/index.html", context)

def buscar_dados():
    request = requests.get("http://127.0.0.1:8000/api/music/?format=json")
    todos = json.loads(request.text)
    print("\n\n\n\n\n\n\n")
    print(todos)
    print("\n")
    print(todos[0]['nome'])
    print("\n\n\n\n\n\n\n")

if __name__ == '__main__':
    buscar_dados()