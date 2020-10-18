from django.conf import settings as project_settings


class Settings:
    def __init__(self, settings: tuple, app_prefix: str = None, defaults: dict = None, internal_settings: dict = None):
        self.settings = settings
        self.defaults = defaults or {}
        self.internal_settings = internal_settings or {}
        self.app_prefix = app_prefix.upper() or ''

    def __getattr__(self, attr):
        if attr not in self.settings and attr not in self.internal_settings:
            raise AttributeError("Missing {} setting: {}".format(self.app_prefix, attr))

        # We use this to search for setting in the project level settings.py with app prefix or not
        project_level_setting = '_'.join([self.app_prefix, attr]) if self.app_prefix else attr

        # Search for the setting in project and in internal app settings.
        if hasattr(project_settings, project_level_setting):
            val = getattr(project_settings, project_level_setting)
        elif self.internal_settings.get(attr):
            val = self.internal_settings[attr]
        else:
            # Fall back to defaults if not found
            val = self.defaults.get(attr)

        self.validate_setting(attr, val)

        # Cache the setting
        setattr(self, attr, val)
        return val

    def validate_setting(self, attr, val):
        if val is None and attr in self.settings:
            raise AttributeError("Translate setting: %r is mandatory" % (attr))
