from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "call_centre"

    def ready(self):
        import_module("call_centre.receivers")
