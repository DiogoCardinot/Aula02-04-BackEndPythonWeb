from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('alunos/', views.ConectaBaseDados, name='listar_alunos'),
    path('usuariosAPI/', views.ConsumirAPI, name='usuariosAPI'),
]