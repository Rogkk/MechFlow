from django.urls import path
from . import views

app_name = 'cadastros'

urlpatterns = [
    path('', views.cadastros_index, name='cadastros_index'),
    path('voltar/', views.cadastros_voltar, name='cadastros_voltar'),
    path('clientes/', views.cadastros_clientes, name='cadastros_clientes'),
    path('cadastro_cliente/', views.cadastros_novo_cliente, name='cadastros_novo_cliente'),
    path('remover_cliente/<int:id>', views.cadastros_remover_cliente, name='cadastros_remover_cliente'),
    path('editar_cliente/<int:id>', views.cadastros_editar_cliente, name='cadastros_editar_cliente')
]
