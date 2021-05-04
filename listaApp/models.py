from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    data_criacao = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    data_termino = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo

class ImagemUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='profile_pics', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'
