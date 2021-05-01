# Create your models here.

from django.db import models
from django.utils import timezone

# Tipo (ex: Trabalho, Estudo, etc...)


class Categoria(models.Model):
    tipo = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")

    def __str__(self):
        return self.tipo  # retorna o nome da categoria quando chamada

# Lista com suas respectivas caracteristicas, pegadno categoria como FOREIGN KEY


class Lista(models.Model):
    titulo = models.CharField(max_length=300)
    conteudo = models.TextField(blank=True)
    data_criacao = models.DateField(
        default=timezone.now().strftime("%Y-%m-%d"))
    data_termino = models.DateField(
        default=timezone.now().strftime("%Y-%m-%d"))
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
