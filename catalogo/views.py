from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CadastroForm
from django.contrib.auth.models import User
from .models import Perfil
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'catalogo/home.html')

def login_view(request):
    if request.method != 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')

    context = {'form': form}
    return render(request, 'catalogo/login.html', context)

def cadastro(request):
    if request.method != 'POST':
        form = CadastroForm()
    else:
        form = CadastroForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password = form.cleaned_data['password'])
                perfil = Perfil.objects.create(user=user, tipo_usuario=form.cleaned_data['tipo_usuario'])
                user.save()
                perfil.save()
                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect('login_view')
            else:
                messages.error(request, 'As senhas não conferem!')
        else:
            messages.error(request, 'Erro ao cadastrar usuário. Verifique os dados e tente novamente.')

    context = {'form': form}
    return render(request, 'catalogo/cadastro.html', context)

def ver_filmes(request):
    return render(request, 'catalogo/verFilmes.html')

def adicionar_filme(request):
    return render(request, 'catalogo/adicionarFilme.html')