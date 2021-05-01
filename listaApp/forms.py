from django import forms
from .models import *
from django.contrib.auth.models import User


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('tipo',)
        widgets = {
            'tipo': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control form-control-user', 'id': 'exampleInputName',
                       'placeholder': ''})
        }


class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ('titulo', 'conteudo', 'data_termino', 'categoria')
        widgets = {
            'titulo': forms.TextInput(
                attrs={'type': 'text', 'nome': 'titulo', 'placeholder': 'Titulo'}),
            'conteudo': forms.TextInput(
                attrs={'type': 'text', 'nome': 'conteudo', 'placeholder': 'Conteudo'}),
            'data_termino': forms.TextInput(
                attrs={'type': 'date', 'nome': 'date'}),
            'categoria': forms.Select(
                attrs={'nome': 'categoria'}),
        }