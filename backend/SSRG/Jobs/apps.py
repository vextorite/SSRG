from django.apps import AppConfig


class MainConfig(AppConfig):
    """
    A class used to configure the Jobs application in django

    ...

    Attributes
    ----------
    default_auto_field : str
        a string indicating which auto field to be used
    name: str
        the name of the Django app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Jobs'