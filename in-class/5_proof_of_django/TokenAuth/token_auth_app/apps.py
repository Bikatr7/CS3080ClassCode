from django.apps import AppConfig


class TokenAuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'token_auth_app'

    def ready(self):
        import token_auth_app.signals
