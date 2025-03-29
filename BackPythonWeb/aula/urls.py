from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home, name='home'),
    path('alunos/', views.ConectaBaseDados, name='listar_alunos'),
    path('usuariosAPI/', views.ConsumirAPI, name='usuariosAPI'),
    path('restrito/', views.PaginaRestrita, name='restrito'),
    path('logout/', views.LogoutView, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='aula/login.html'), name='login'), 
    path('buscar_alunos/', views.BuscarAlunos, name='buscar_alunos'),
]