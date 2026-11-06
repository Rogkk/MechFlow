from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cadastros_index(request):
    return render(request, 'cadastros/cadastros_view.html')

def cadastros_voltar(request):
    return render(request, 'dashboard/dashboard_view.html')

def cadastros_clientes(request):
    return render(request, 'cadastros/cadastros_clientes_view.html')
