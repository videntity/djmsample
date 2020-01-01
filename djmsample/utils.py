from decimal import Decimal
from django.conf import settings

TRUE_LIST = [1, "1", "true", "True", "TRUE", "YES", "Yes", "yes", True]
FALSE_LIST = [0, "0", "False", "FALSE", "false", "NO", "No", "no", False]


def bool_env(env_val):
    """ check for boolean values """

    if env_val:
        if env_val in TRUE_LIST:
            return True
        if env_val in FALSE_LIST:
            return False
        return env_val
    else:
        if env_val in FALSE_LIST:
            return False
        return


def int_env(env_val):
    """ convert to integer from String """

    return int(Decimal(float(env_val)))


"""
Create a function that will perform a contextprocessor function and
return a True or False based on whether an app is in settings.INSTALLED_APPS

The purpose is to simplify Environment/Installation Specific code branching

Installation Specific code should be islated to an app that is embedded
in the list of installed apps.
Custom HTML should be installed in the templates/{app_Name} folder inside
the application.

"""


def IsAppInstalled(target_app=None):
    """ Is an app in INSTALLED_APPS """

    if target_app:
        if target_app in settings.INSTALLED_APPS:
            return True
    # Return False if target_app is not defined
    # or target_app is not found in INSTALLED_APPS
    return False


def active_apps(request):
    """ Is app active in INSTALLED_APPS """

    return {'active_apps': settings.INSTALLED_APPS}
