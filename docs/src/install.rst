Install and configure
=====================

1. Install Centrifugo:

Download it `here <https://github.com/centrifugal/centrifugo/releases>`_

.. highlight:: bash

::

   unzip centrifugo-1.x.x.zip
   cd centrifugo-1.x.x


2. Configure Centrifugo

::

   ./centrifugo genconfig
   
This will generate your secret key in a ``config.json`` file. Edit it and set anonymous to true if you want 
to use public events. Leave it if you want only the logged in users to receive the events.

.. highlight:: javascript

::

   {
  "secret": "70b651f6-775a-4949-982b-b387b31c1d84",
  "anonymous": true
  }

3. Install Django Instant:

::

   pip install django-instant
   
   
Add to installed apps:

::

   "instant",

Set the urls:

.. highlight:: python

::
   # required only if you want to use the frontend at /instant/
   url('^instant/', include('instant.urls')),

Settings
~~~~~~~~

Configure settings.py:

::

   # required settings
   CENTRIFUGO_SECRET_KEY = "70b651f6-775a-4949-982b-b387b31c1d84" # the_key_that_is_in_config.json
   SITE_SLUG = "my_site" # used internaly to prefix the channels
   SITE_NAME = "My site"
   
   # optionnal settings
   CENTRIFUGO_HOST = 'http://ip_here' #default: localhost
   CENTRIFUGO_PORT = 8012 # default: 8001
   INSTANT_PUBLIC_CHANNEL = "public" #default: SITE_SLUG+'_public'
   INSTANT_ENABLE_PUBLIC_CHANNEL = False # this one is to disable the default public channel
   
By default the events are published using python. A go module is available to perform the publish
operations in order to leave the main process alone as much as possible. This might be usefull when lots of messages
are sent. 

Note: when this option is enabled there is no error handling. This option is recommended when you need higher performance
and don't care about error messages.

You might have to make the `instant/go/publish` file executable with `chmod`

::

   INSTANT_BROADCAST_WITH = 'go'
   
Performance test: 1000 messages:

- Python: 2.96 seconds
- Go: 1.41 seconds

10000 messages:

- Python: 29.57 seconds
- Go: 14.44 seconds

Note: this test uses the standard publish function so that each new event sent makes an new connection to Centrifugo.

Templates
~~~~~~~~~

Include the template ``{% include "instant/client.html" %}`` anywhere: nothing will be displayed it is the engine. 
See next section for messages handling. 
