from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

# Login do sistema
def login(request):
    return render(request, 'registration/login.html')   

# Página principal
@login_required
def index(request):
    if request.method == 'POST':
        form = ListaForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.usuario = request.user
            newform.save()
            return redirect('index')
    else:
        form = ListaForm()
    lista = Lista.objects.filter(usuario=request.user)
    qtd_lista = len(lista)
    lista = reversed(lista)
    return render(request, 'index.html', {'form': form, 'listas': lista, 'qtd_lista': qtd_lista })

# Excluir item da lista
@login_required
def excluir_item(request, id):
    item = Lista.objects.get(pk=id)
    item.delete()
    return redirect('index')

# Cadastrar categoria //A fazer
@login_required
def cadastro_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
        return redirect('index')

# Cadastrar usuario
def user(request):
    return render(request, 'registro-usuario.html')

@require_POST
def registro_usuario(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])
        if usuario_aux:
            return render(request, 'caminho para o index', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail'})
    except User.DoesNotExist:
        nome_usuario = request.POST['nome-usuario']
        email = request.POST['email']
        senha = request.POST['senha']
        novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
        novoUsuario.save()
        return redirect('user')
