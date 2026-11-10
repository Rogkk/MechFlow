from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .forms import ParticipanteForm
from .models import ParticipanteModel

# Create your views here.
def cadastros_index(request):
    return render(request, 'cadastros/cadastros_view.html')

def cadastros_voltar(request):
    return render(request, 'dashboard/dashboard_view.html')

def cadastros_remover_cliente(request:HttpRequest, id):
    cliente = get_object_or_404(ParticipanteModel, id=id)
    cliente.delete()
    return redirect('cadastros:cadastros_clientes')

def cadastros_editar_cliente(request:HttpRequest, id):
    cliente = get_object_or_404(ParticipanteModel, id=id)
    if request.method == 'POST':
        form = ParticipanteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cadastros:cadastros_clientes')

    form = ParticipanteForm(instance=cliente)
    context = {
        'form': form
    }
    return render(request, 'cadastros/cadastros_novo_cliente_view.html',
        context)

def cadastros_clientes(request):
    context = {
        "clientes": ParticipanteModel.objects.all()
    }
    return render(request, 'cadastros/cadastros_clientes_view.html', context)

def cadastros_novo_cliente(request:HttpRequest):
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastros:cadastros_clientes')

    context = {
        'form': ParticipanteForm(initial={
            'eh_cliente': True,
        })
    }
    return render(request, 'cadastros/cadastros_novo_cliente_view.html', context)
