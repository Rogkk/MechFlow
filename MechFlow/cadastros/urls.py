from django.urls import path
from . import views

app_name = 'cadastros'

urlpatterns = [
    path('', views.cadastros_index, name='cadastros_index'),
    path('voltar/', views.cadastros_voltar, name='cadastros_voltar'),
    path('clientes/', views.cadastros_clientes, name='cadastros_clientes')
]
