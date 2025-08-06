from django.shortcuts import render
from django.http import HttpResponse
from .forms import CadastroForm

# Create your views here.
def home(request):
    return render(request, 'catalogo/home.html')

def login(request):
    return render(request, 'catalogo/login.html')

def cadastro(request):
    if request.method != 'POST':
        form = CadastroForm()

    context = {'form': form}
    return render(request, 'catalogo/cadastro.html', context)