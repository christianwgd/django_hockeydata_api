django-hockeydata-api
=====================


A Django package for simple use of Hockeydata Javascript API (https://apidocs.hockeydata.net/).


Requirements
------------


- Python 2.7+, 3.6+
- Django >= 1.11 (tested with this, earlier versions might work also)
- For details, see https://docs.djangoproject.com/en/dev/faq/install/#faq-python-version-support


Installation
------------

1. Install using pip (not available at this time, TODO):

   ``pip install git+https://git.wgdnet.de/cwiegand/django_hockeydata_api.git``

   Alternatively, you can install download or clone this repo and
   call ``pip install -e .``.

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

    <!-- Hockeydata javascript -->
    {% hockeydata_js 'los_player_fullpage' %}

    <!-- Hockeydata Widget -->
    {% hockeydata_widget widgetName='hockeydata.los.Player.FullPage'
                         divisionId='<yourDivisionId>' playerId=playerId %}
    {% endblock %}

    {% block content %}
    <div id='#player'></div>
    {% endblock %}


Documentation
-------------

The Templatetags can receive almost all hockeydata widget options, just write
them down in python syntax (e.g. true --> True).
At the moment there is one special option for the game slider widget to get
the gameLink parameter from a callback function. This is useful if you want
a gameslider for multiple divisions (e.g. for all divsions of an association):

.. code:: Django

    {% hockeydata_widget domNode='#gameslider' widgetName='hockeydata.los.GameSlider'
                         divisionId='<yourDivisionId>' gameLink='/link_to_game/%G/%D'
                         gameLinkFromCallback=True %}

%G will be replaced by Game-ID and %D by Divsion-ID if gameLinkFromCallback
is true.

Some widgets support a callback function, that is called when all javascript
is done and the widget is built. Set this option as simple string (e.g ``paint``
instead of ``paint()``). If no javascript function with this name exists,
the option is ignored.

hockeydata api documentation: http://apidocs.hockeydata.net/
hockeydata widget reference: https://apidocs.hockeydata.net/javascript-api/

Settings
########

The django-hockeydata-api requires some pre-configured settings.

They can be modified by adding a dict variable called ``HOCKEYDATA`` in your
``settings.py`` and customizing the values ​​you want;

The ``HOCKEYDATA`` dict variable contains these settings:

.. code:: python

    # hockeydata_api settings
    HOCKEYDATA = {
        # Hockeydata Api-Key (you can get it from https://apidocs.hockeydata.net/api-key/)
        'API_KEY': '',

        # Sport definition key: americanfootball|icehockey
        'SPORT': 'icehockey',

        # Base-URL to hockeydata static javascript and css
        'STATIC': 'https://api.hockeydata.net/',

        # Default template: los_template_dark|los_template_glass|los_template_default
        'DEFAULT_CSS': 'los_template_dark',

        # localization i18n_x_los, where x is the ISO-639-1 language code (de = Germany)
        # https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
        'I18N': 'i18n_de_los',

        # Base divison of organisation (e.g. association, club etc.)
        # you can get this id from here: https://apidocs.hockeydata.net/division-finder/
        # 1900 is the actual sample of austrian EBEL, which is also used for the hockeydata samples
        'BASE_DIV': '1900',
    }

Example app
-----------

The example app is created for running with django 2.0+!

1. create virtualenv

2. install django with 'pip install django'.
   See https://www.djangoproject.com/ for more information.

3. install django_hockeydata_api as described above

4. copy example app to a folder of your choice

5. set the EXAMPLE_DIV and EXAMPLE_DIV in settings.py to suitable division-ids

6. run using 'python manage.py runserver'. No database or user is required,
so you can skip 'python manage.py migrate'.


Bugs and suggestions
--------------------

If you have found a bug or if you have a request for additional functionality,
please use the issue tracker on the project:

https://git.wgdnet.de/cwiegand/django_hockeydata_api/issues


License
-------

You can use this under BSD-License. See `LICENSE <LICENSE>`_ file for details.
