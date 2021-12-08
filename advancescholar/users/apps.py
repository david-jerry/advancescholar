from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "advancescholar.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import advancescholar.users.signals  # noqa F401
        except ImportError:
            pass
