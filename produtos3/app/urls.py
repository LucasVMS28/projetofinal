from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ProdutoUpdateView, registrar_usuario

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('busca/', views.busca, name='busca'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
    path('produto/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_editar'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='form'),
     path('usuario/', registrar_usuario, name='usuario')
]