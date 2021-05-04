from django.apps import AppConfig


class ListaappConfig(AppConfig):
    name = 'listaApp'

    def ready(self):
        import listaApp.signals