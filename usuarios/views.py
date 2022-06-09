from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            return redirect('cadastro')
        if not email.strip():
            return redirect('cadastro')
        if senha != senha2:
            redirect('cadastro')
        if User.objects.filter(email=email).exists():
            redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            return render(request, 'usuarios/login.html')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')

def cria_receita(request):
    return render(request, 'usuarios/cria_receita.html')