from django.apps import AppConfig


class MainConfig(AppConfig):
    """
    A class used to configure the Jobs application in django

    ...

    Attributes
    ----------
    none
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Jobs'