django-app-settings
===================

This package allows the apps to set its own settings and search for them in the project with the specified prefix.
This approach makes it convenient to implement app settings in any project with classic way and not spend time to write your own settings module.

In `Adding to your app`_ section described the way how you can use this package in your own app.

In `Project level usage`_ section you will be informed about what you need to tell to your app users to set the settings correct.


Installation
------------

1. Clone repo:

.. code-block:: console

    git clone https://github.com/1mace1/django-app-settings.git

2. Change directory:

.. code-block:: console

    cd django-app-settings/

2. Make a package:

.. code-block:: console

    python setup.py sdist

3. Install with pip:

.. code-block:: console

    pip install dist/django-app-settings-*.tar.gz

4. Add `django-app-settings` to your package requirements


Adding to your app
------------------

1. Import ``Settings`` in to your app settings.py:

.. code-block:: python

    from django_app_settings import Settings

2. Set the settings names that are required in your app and defaults for them:

.. code-block:: python

    settings = (
        'SETTING1',
        'SETTING2'
    )
    defaults = {
        'SETTING1': 'value'
    }

.. warning::
    All the settings names should be uppercase!

.. note::
    ``defaults`` is unnecessary

3. Set the ``settings_prefix`` in order to be able to find your settings at the project level:

.. code-block:: python

    settings_prefix = 'MYAPP'

4. create ``Settings`` object:

.. code-block:: python

    app_settings = Settings(settings, settings_prefix, defaults)

Summing up, your settings.py should be:

.. code-block:: python

    from django_app_settings import Settings

    settings_prefix = 'MY_APP'
    settings = (
        'SETTING1',
        'SETTING2'
    )
    defaults = {
        'SETTING1': 'value'
    }

    app_settings = Settings(settings, defaults, settings_prefix)

Usage in app
''''''''''''

For now, you can import ``app_settings`` anywhere and use as below

.. code-block:: python

    from your_app.settings import app_settings

    app_settings.SETTING1

All the settings in ``settings`` tuple are **mandatory**. So if default value for particular setting are not specified and there is no setting in project level, the user will get an error.
Therefore, please, warn users of your app to set the required settings as shown below in `Project level usage`_.

Project level usage
-------------------

People who will use your app with this package should set settings in their project level **settings.py** with your ``settings_prefix``.
So if your ``settings_prefix`` is ``SOME_APP`` as above then project level settings should be:

.. code-block:: python

    MY_APP_SETTING1 = 'some value'
    MY_APP_SETTING1 = 'another value'

