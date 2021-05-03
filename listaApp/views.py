from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    lista = Lista.objects.all()
    lista = reversed(lista)
    if request.method == 'POST':
        form = ListaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ListaForm()
    return render(request, 'index.html', {'form': form, 'listas': lista })

def excluir_item(request, id):
    item = Lista.objects.get(pk=id)
    item.delete()
    return redirect('index')
