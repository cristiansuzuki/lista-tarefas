from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('excluir-item/<id>', views.excluir_item, name='excluir-item'),
    path('login', views.login, name='login'),
    path('user', views.user, name='user'),
    path('registro-usuario', views.registro_usuario, name='registro-usuario'),
]
