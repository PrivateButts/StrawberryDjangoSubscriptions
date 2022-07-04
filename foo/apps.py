from django.apps import AppConfig


class FooConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foo'
    def ready(self):
        from . import signals