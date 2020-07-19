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

2. Set the settings names that are required in your app:

.. code-block:: python

    settings = (
        'SETTING1',
        'SETTING2',
        ...
    )

.. warning::
    All the settings names should be uppercase!

3. (optional) Set ``defaults`` for your settings so that the setting can fall back to defaults if it is not found in project:

.. code-block:: python

    defaults = {
        'SETTING1': 'value',
        ...
    }

4. (optional) Set the ``app_prefix`` in order to be able to find your settings in the project using this prefix:

.. code-block:: python

    app_prefix = 'MYAPP'

.. note::

    This is an optional step, so you don't have to set app_prefix,
    but I strongly recommend you do this so that there are no conflicts with other project settings

5. (optional) If you have constant settings that don't need to be changed, you can use internal_settings.
   User at the project level will not have access to these settings:

.. code-block:: python

    internal_settings = {
        'INTERNAL1': 'VALUE1',
        ...
    }


6. Create ``Settings`` object:

.. code-block:: python

    app_settings = Settings(settings, app_prefix=app_prefix, defaults=defaults, internal_settings=internal_settings)

Summing up, your settings.py should be:

.. code-block:: python

    from django_app_settings import Settings

    app_prefix = 'MY_APP'
    settings = (
        'SETTING1',
        'SETTING2'
    )
    defaults = {
        'SETTING1': 'value'
    }
    internal_settings = {
        'INTERNAL1': 'VALUE1',
    }

    app_settings = Settings(settings, app_prefix=app_prefix, defaults=defaults, internal_settings=internal_settings)

You can skip the optional steps and set the ``settings`` only so that your ``app_settings`` are like this:

.. code-block:: python

    from django_app_settings import Settings

    settings = (
        'SETTING1',
        'SETTING2'
    )

    app_settings = Settings(settings)


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

People who will use your app with this package should set settings in their project level **settings.py** with your ``app_prefix`` or just leave them.
So if your ``app_prefix`` is ``SOME_APP`` as above then project level settings should be:

.. code-block:: python

    MY_APP_SETTING1 = 'some value'
    MY_APP_SETTING2 = 'another value'

