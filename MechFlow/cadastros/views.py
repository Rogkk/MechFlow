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

def cadastros_novo_participante(request:HttpRequest):

    context = {
        'form': ParticipanteForm()
    }
    
    return render(request, 'cadastros/cadastros_novo_participante_view.html', context)





