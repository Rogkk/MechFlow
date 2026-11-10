from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import ParticipanteForm

# Create your views here.
def cadastros_index(request):
    return render(request, 'cadastros/cadastros_view.html')

def cadastros_voltar(request):
    return render(request, 'dashboard/dashboard_view.html')

def cadastros_clientes(request):
    return render(request, 'cadastros/cadastros_clientes_view.html')

def cadastros_novo_cliente(request:HttpRequest):
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cadastros/cadastros_clientes_view.html')

    context = {
        'form': ParticipanteForm()
    }
    return render(request, 'cadastros/cadastros_novo_cliente_view.html', context)
