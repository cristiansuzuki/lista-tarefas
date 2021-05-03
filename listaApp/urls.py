from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('excluir-item/<id>', views.excluir_item, name='excluir-item')
]
