from django.shortcuts import render

# Create your views here.
from multiprocessing import context
from turtle import title
from django.shortcuts import render

import reembolsos
from reembolsos.models import Reembolso
from .models import Reembolso


def index(request):
    return render(request, 'index.html')


def reembolso(request):
    reembolsos = Reembolso.objects.order_by('-data_cadastro').all()

    nome = request.GET.get('busca')

    if nome != '' and nome is not None:
        reembolsos = reembolsos.filter(nome=nome)

    dados = {
        'reembolsos': reembolsos
    }

    return render(request, 'reembolso.html', dados)

