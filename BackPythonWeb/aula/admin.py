from django.contrib import admin
from .models import Aluno

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'email', 'data_de_nascimento', 'data_de_criacao')
    search_fields = ('nome', 'email') 
    list_filter = ('idade',)
    ordering = ('data_de_criacao',)

admin.site.register(Aluno, AlunoAdmin)