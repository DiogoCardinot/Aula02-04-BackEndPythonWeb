from django.shortcuts import render
from .models import Aluno
import requests

def Home(request):
    return render(request, 'aula/aula.html')

# Acesso aos dados da base de dados
def ConectaBaseDados(request):
    alunos = Aluno.objects.all()
    context={
        'alunos' : alunos,
    }

    return render(request, 'aula/alunos.html', context)

# Conexão e consumo de dados com API
def ConsumirAPI(request):
    url = 'https://jsonplaceholder.typicode.com/users'
    resposta = requests.get(url)
    usuariosAPI = resposta.json() 
    context = {
        'usuariosAPI': usuariosAPI
    }
    return render(request, 'aula/ConsumirAPI.html', context)