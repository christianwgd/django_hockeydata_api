=====================
django_hockeydata_api
=====================

A Django package for simple use of Hockeydata Javascript API (https://apidocs.hockeydata.net/).


Requirements
------------

- Python 2.7+, 3.6+
- Django >= 1.11 (tested with this, earlier versions might work also)
- For details, see https://docs.djangoproject.com/en/dev/faq/install/#faq-python-version-support


Installation
------------

1. Install using pip:

   ``pip install django_hockeydata_api``

   Alternatively, you can install download or clone this repo and call ``pip install -e .``.

2. Add to INSTALLED_APPS in your ``settings.py``:

   ``'hockeydata_api',``

3. In your templates, load the ``widget_tags`` library:


Example template
----------------

   .. code:: Django

    {% load widget_tags %}

    {% block extra_head_content %}
    {{ block.super }}
    <!-- Hockeydata css -->
    {% hockeydata_css 'los_player_fullpage' %}
    <!-- custom widget css -->
    <link href="{% static 'js/style.css' %}" rel="stylesheet">

    <!-- Hockeydata Javascript -->
    {% hockeydata_js 'los_player_fullpage' %}
    {% endblock %}

    {% block content %}
    <div>
        {% hockeydata_widget widgetName='hockeydata.los.Player.FullPage' divisionId='nev-vln-hr' playerId=playerId %}
    </div>
    {% endblock %}


Documentation
-------------

TODO


Bugs and suggestions
--------------------

If you have found a bug or if you have a request for additional functionality, please use the issue tracker on GitHub.

https://git.wgdnet.de/cwiegand/django_hockeydata_api/issues


License
-------

You can use this under BSD-License. See `LICENSE <LICENSE>`_ file for details.