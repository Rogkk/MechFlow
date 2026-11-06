from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .forms import TarefaForm
from .models import TarefaModel
# Create your views here.

def tarefas_home(request):
    contexto = {
        "nome":"Rogerio",
        "tarefas":TarefaModel.objects.all()
    }
    return render(request, 'tarefas/index.html', contexto)

def adicionar(request:HttpRequest):
    if request.method == 'POST':
        formulario = TarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:home')

    contexto = {
        'form':TarefaForm
    }
    return render(request, 'tarefas/adicionar.html', contexto)

def remover(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    tarefa.delete()
    return redirect('tarefas:home')

def editar(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    if request.method == "POST":
        formulario = TarefaForm(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:home')

    formulario = TarefaForm(instance=tarefa) # formulario com dados inserido
    contexto = {
        'form':formulario
    }
    return render(request, 'tarefas/editar.html', contexto)
