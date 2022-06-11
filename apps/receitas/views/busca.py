from ..models import Receita
from django.shortcuts import get_object_or_404, redirect, render

def busca(request):
    receitas_buscadas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            receitas_buscadas = receitas_buscadas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': receitas_buscadas
    }

    return render(request, 'receitas/buscar.html', dados)