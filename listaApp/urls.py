from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('excluir-item/<id>', views.excluir_item, name='excluir-item'),
    path('login', views.login, name='login'),
    path('user', views.user, name='user'),
    path('registro-usuario', views.registro_usuario, name='registro-usuario'),
    path('page-error', views.page_error, name='page-error'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
