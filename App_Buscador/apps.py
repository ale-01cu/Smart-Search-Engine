from django.apps import AppConfig


class AppBuscadorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'App_Buscador'


    def ready(self):
        import App_Buscador.helpers.indices