from django.shortcuts import render,  redirect
from .models import Aluno
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


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


@login_required(login_url='/aula/login/')
def PaginaRestrita(request):
    return render(request, 'aula/restrito.html')

def LogoutView(request):
    logout(request)
    return redirect('login')