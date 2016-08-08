Install and configure
=====================

Instant can deliver events in real time to the users. This is made using the 
`Centrifugo <https://github.com/centrifugal/centrifugo/>`_  websockets server.
 
**Warning**: this app is still at an early alpha stage.

1. Install Centrifugo: example for Debian: 

.. highlight:: bash

::

   sudo apt-get install golang
   mkdir go && cd go
   wget https://github.com/centrifugal/centrifugo/releases/download/v1.5.1/centrifugo-1.5.1-linux-386.zip
   unzip centrifugo-1.5.1-linux-386.zip
   cd centrifugo-1.5.1-linux-386


2. Configure Centrifugo

::

   ./centrifugo genconfig
   
This will generate your secret key. Set anonymous to true if you want all users to receive the messages. 
Leave it if you want only the logged in users to see the messages.

.. highlight:: javascript

::

   {
  "secret": "70b651f6-775a-4949-982b-b387b31c1d84",
  "anonymous": true
  }

3. Install the python requirements:

::

   pip install cent
   cd my_django_project_root
   git clone https://github.com/synw/django-instant.git
   mv django-instant/instant . && rm -rf django-instant
   
In settings.py add to ``INSTALLED_APPS``:

   .. highlight:: python

::

   "instant",

Set the urls:

.. highlight:: python

::

   url('^instant/', include('instant.urls')),
   
4. Install the js part with npm:

.. highlight:: python

::

   cd static && mkdir instant && cd instant
   npm install centrifuge

Settings
~~~~~~~~

Add ``'instant',`` to installed apps and configure settings.py:

::

   # required settings
   SITE_SLUG = "my_site" # used internaly to prefix the channels
   CENTRIFUGO_SECRET_KEY = "the_key_that_is_in_config.json"
   # optionnal settings
   CENTRIFUGO_HOST = 'http://ip_here' #default: localhost
   CENTRIFUGO_PORT = 8012 # default: 8001

Templates
~~~~~~~~~

Include the template ``{% include "instant/client.html" %}`` anywhere (nothing will be displayed it is the engine), 
in the footer for example. Add ``{% include "instant/messages.html" %}`` where you want the message counter to be.
