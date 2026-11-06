from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.tarefas_home, name='home'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('remover/<int:id>', views.remover, name='remover'),
    path('editar/<int:id>', views.editar, name='editar')
]