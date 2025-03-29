from django.shortcuts import render,  redirect
from .models import Aluno
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db import connection


def Home(request):
    return render(request, 'aula/aula.html')

# Acesso aos dados da base de dados
def ConectaBaseDados(request):
    alunos = Aluno.objects.all()
    total_alunos = Aluno.objects.all().count()
    context={
        'alunos' : alunos,
        'total_alunos': total_alunos
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

# Autenticacao necessaria para acessar a pagina
@login_required(login_url='/aula/login/')
def PaginaRestrita(request):
    return render(request, 'aula/restrito.html')

# Redirecionamento do logout
def LogoutView(request):
    logout(request)
    return redirect('login')

# ORM x SQL
def BuscarAlunos(request):
    # Busca usando ORM: alunos com idade > 23
    alunos_orm = Aluno.objects.filter(idade__gt=23)
    # Quantidade de alunos com idade > 23
    alunos_orm_total = Aluno.objects.filter(idade__gt=23).count()

    # Busca usando SQL puro: alunos com idade <= 23
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, nome, idade, email, data_de_nascimento FROM aula_aluno WHERE idade <= 23")
        alunos_sql = [
            {
                "id": row[0],
                "nome": row[1],
                "idade": row[2],
                "email": row[3],
                "data_de_nascimento": row[4],
            }
            for row in cursor.fetchall()
        ]
    
        # Quantidade de alunos com idade <= 23
        cursor.execute("SELECT COUNT(*) FROM aula_aluno WHERE idade <= 23")
        alunos_sql_total = cursor.fetchone()[0]

    context = {
        'alunos_orm': alunos_orm,
        'alunos_orm_total':alunos_orm_total,
        'alunos_sql': alunos_sql,
        'alunos_sql_total': alunos_sql_total,
    }

    return render(request, 'aula/buscar_alunos.html', context)