from django.shortcuts import render
from datetime import datetime

def index(request):
    contexto = { "titulo": "Instituto Federal do Piauí",
                 "subtitulo" : "Turma 2016",
                 "menu" : ['home', 'sobre', 'porfólio', 'produtos', 'FAQ', 'contato']}

    return render(request, 'index.html', contexto)
