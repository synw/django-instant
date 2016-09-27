Install and configure
=====================

1. Install Centrifugo:

.. highlight:: bash

::

   wget https://github.com/centrifugal/centrifugo/releases/download/v1.5.1/centrifugo-1.5.1-linux-386.zip
   unzip centrifugo-1.5.1-linux-386.zip
   cd centrifugo-1.5.1-linux-386


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

3. Install:

::

   pip install django-instant

Set the urls:

.. highlight:: python

::

   url('^instant/', include('instant.urls')),

Settings
~~~~~~~~

Add ``'instant',`` to installed apps and configure settings.py:

::

   # required settings
   CENTRIFUGO_SECRET_KEY = "70b651f6-775a-4949-982b-b387b31c1d84" # the_key_that_is_in_config.json
   SITE_SLUG = "my_site" # used internaly to prefix the channels
   SITE_NAME = "My site"
   
   # optionnal settings
   CENTRIFUGO_HOST = 'http://ip_here' #default: localhost
   CENTRIFUGO_PORT = 8012 # default: 8001
   INSTANT_PUBLIC_CHANNEL = "public" #default: SITE_SLUG+'_public'

Templates
~~~~~~~~~

Include the template ``{% include "instant/client.html" %}`` anywhere: nothing will be displayed it is the engine. 

Add ``{% include "instant/messages.html" %}`` where you want the message counter to be.
