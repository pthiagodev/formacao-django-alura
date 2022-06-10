from unicodedata import name
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            messages.error(request, 'O campo não pode ficar vazio')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, 'O campo não pode ficar vazio')
            return redirect('cadastro')
        if senhas_diferentes(senha, senha2):
            messages.error(request, 'As senhas não são iguais!')
            return redirect('cadastro')
        if email_ja_cadastrado(email):
          messages.error(request, 'O e-mail já está cadastrado!')
          return redirect('cadastro')
        if nome_ja_cadastrado(nome):
           messages.error(request, 'O nome de usuário já está cadastrado!')
           return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'E-mail ou senha não informados!')
            return render(request, 'usuarios/login.html')
        if email_ja_cadastrado(email):
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Usuário logado com sucesso!')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        receitas = Receita.objects.order_by('-data_receita').filter(enviado_por=request.user.id)

        dados = {
            'receitas' : receitas
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def campo_vazio(campo):
    return not campo.strip()

def senhas_diferentes(senha, senha2):
    return senha != senha2

def nome_ja_cadastrado(nome):
    return User.objects.filter(username=nome).exists()
        
def email_ja_cadastrado(email):
    return User.objects.filter(email=email).exists()