from django.apps import AppConfig


class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
