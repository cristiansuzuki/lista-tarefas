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
        fields = ('titulo', 'conteudo',
                  'data_termino', 'categoria')
        widgets = {
            'titulo': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control form-control-user', 'id': 'exampleInputName',
                       'placeholder': 'Digite o título'}),
            'conteudo': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control form-control-user', 'id': 'exampleInputName',
                       'placeholder': 'Digite o conteúdo'}),
            'data_termino': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control form-control-user', 'id': 'exampleInputDate',
                       'placeholder': ''}),
            'categoria': forms.Select(
                attrs={'type': 'select', 'class': 'form-control form-control-user', 'id': 'exampleInputSelect',
                       'placeholder': ''}),
        }
