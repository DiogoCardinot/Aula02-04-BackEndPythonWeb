from django.db import models

# BASE DE DADOS ALUNO
class Aluno(models.Model):
    nome = models.CharField(max_length=100)  
    idade = models.IntegerField()            
    email = models.EmailField(unique=True)  
    data_de_nascimento = models.DateField() 
    data_de_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome