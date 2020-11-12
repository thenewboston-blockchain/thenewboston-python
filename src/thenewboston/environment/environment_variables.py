import os

from django.core.exceptions import ImproperlyConfigured


def get_environment_variable(name):
    """
    Return the environment variable or return exception
    """

    try:
        return os.environ[name]
    except KeyError:
        raise ImproperlyConfigured(f'Set the {name} environment variable')
