from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users"
    verbose_name: _("Users")

    def ready(self) -> None:
        """
        Function for user model and profile signals.
        """
        try:
            # from . import signals
            import apps.users.signals
        except ImportError:
            pass
