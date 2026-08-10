from django.urls import path
from .views import home,detalhe,novo_projeto,editar_projeto,excluir_projeto

urlpatterns = [
    path('',home,name='home'),
    path("projeto/<int:id>/",detalhe,name='detalhe'),
    path("novo-projeto/",novo_projeto,name='novo_projeto'),
    path("editar-projeto/<int:id>/",editar_projeto,name='editar_projeto'),
    path("excluir-projeto/<int:id>/",excluir_projeto,name='excluir_projeto'),
]