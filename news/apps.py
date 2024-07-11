from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
    verbose_name = 'Новости'

    def ready(self):
            """Register all signals."""
            # Implicitly connect a signal handlers decorated with @receiver.
            from . import signals
