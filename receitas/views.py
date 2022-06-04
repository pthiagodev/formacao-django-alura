from django.shortcuts import render

def index(request):

    receitas = {
        1: 'Pastel',
        2: 'Lasanha',
        3: 'Coxinha',
        4: 'Pizza',
        5: 'Esfiha',
        6: 'Calzone'
    }

    dados = {
        'nome_das_receitas': receitas
    }

    return render(request, 'index.html', dados)

def receita (request):
    return render(request, 'receita.html')
