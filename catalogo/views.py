from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CadastroForm
from django.contrib.auth.models import User
from .models import Perfil

# Create your views here.
def home(request):
    return render(request, 'catalogo/home.html')

def login(request):
    return render(request, 'catalogo/login.html')

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
                return redirect('home')
            else:
                messages.error(request, 'As senhas não conferem!')
        else:
            messages.error(request, 'Erro ao cadastrar usuário. Verifique os dados e tente novamente.')

    context = {'form': form}
    return render(request, 'catalogo/cadastro.html', context)