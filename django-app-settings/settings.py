from django.conf import settings as project_settings


class Settings:
    def __init__(self, settings: tuple, app_prefix: str, defaults: dict = None):
        self.settings = settings
        self.defaults = defaults or {}
        self.app_prefix = app_prefix.upper()

    def __getattr__(self, attr):
        if attr not in self.settings:
            raise AttributeError("Missing {} setting: {}".format(self.app_prefix, attr))

        try:
            val = getattr(project_settings, '{}_{}'.format(self.app_prefix, attr), None)
        except KeyError:
            val = self.deafults.get(attr)

        self.validate_setting(attr, val)

        setattr(self, attr, val)
        return val

    def validate_setting(self, attr, val):
        if val is None and attr in self.settings:
            raise AttributeError("Translate setting: %r is mandatory" % (attr))
