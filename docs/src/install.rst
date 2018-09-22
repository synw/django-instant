Install and configure
=====================

1. Install Django Instant:

::

   pip install django-instant
   
   
Add to installed apps:

::

   "corsheaders",
   "instant",
   
2. Install the websockets server

An installer is available for Linux only:

.. highlight:: bash

::

   python3 manage.py installws
   
This will download the Centrifugo websockets server, install it and update your settings.py 
file with the appropriate configuration.

For other systems you have to install 
Centrifugo `manually <https://fzambia.gitbooks.io/centrifugal/content/server/start.html>`_

Settings
~~~~~~~~

Configure the middleware:

::

   MIDDLEWARE = [
      ...
      'corsheaders.middleware.CorsMiddleware',
      'django.middleware.common.CommonMiddleware',
      ...
   ]

Note: if you use the management command to install the server the settings below will already 
be configured.

::

   # required settings
   CENTRIFUGO_SECRET_KEY = "70b651f6-775a-4949-982b-b387b31c1d84" # the_key_that_is_in_config.json
   SITE_SLUG = "my_site" # used internaly to prefix the channels
   SITE_NAME = "My site"
   
   CORS_ORIGIN_WHITELIST = ('localhost:8001',)
   
   # optionnal settings
   CENTRIFUGO_HOST = 'http://ip_here' #default: localhost
   CENTRIFUGO_PORT = 8012 # default: 8001

   
By default the events are published using python. A go module is available to perform the 
publish operations in order to leave the main process alone as much as possible. 
This might be usefull when lots of messages are sent. 

Note: when this option is enabled there is no error handling. This option is recommended 
when you need higher performance and don't care about error messages.

You might have to make the `instant/go/publish` file executable with `chmod`

.. highlight:: python

::

   INSTANT_BROADCAST_WITH = 'go'
   
Performance test: 1000 messages:

- Python: 2.96 seconds
- Go: 1.41 seconds

10000 messages:

- Python: 29.57 seconds
- Go: 14.44 seconds

Note: this test uses the standard publish function so that each new event sent makes an 
new connection to Centrifugo.

Templates
~~~~~~~~~

Include the template ``{% include "instant/client.html" %}`` anywhere: nothing will 
be displayed it is the engine. See next section for messages handling. 

Run the websockets server
~~~~~~~~~~~~~~~~~~~~~~~~~

If you used the installer:

.. highlight:: bash

::

   python3 manage.py runws
   
Otherwise run the Centrifugo server normally

Frontend
~~~~~~~~

A demo frontend is available. To use it:

Set the urls:

.. highlight:: python

::

   from instant.views import instant_auth
   
   urlpatterns = [
   	# ...
   	url(r'^centrifuge/auth/$', instant_auth, name='instant-auth'),
   	url('^instant/', include('instant.urls')),
   	]

Login as superuser and go to `/instant/`
