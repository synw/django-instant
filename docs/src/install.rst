Install and configure
=====================

Instant can deliver events in real time to the users. This is made using the 
`Centrifugo <https://github.com/centrifugal/centrifugo/>`_  websockets server.
 
**Warning**: all this is still experimental. Use at your own risks.

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
   git clone https://github.com/synw/django-mqueue.git
   mv django-mqueue/mqueue . && rm -rf django-mqueue
   python manage.py makemigrations && python manage.py migrate
   
In settings.py add to ``INSTALLED_APPS``:

   .. highlight:: python

::

   "mqueue",
   "instant",

Set the urls:

.. highlight:: python

::

   url('^instant/', include('instant.urls')),
   
4. Install the js part with npm:

.. highlight:: python

::

   cd static/instant
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



Important: if you use the log handler these settings must be placed before ``from mqueue.conf import LOGGING``

Templates
~~~~~~~~~

Include the template ``{% include "instant/stream.html" %}`` anywhere (nothing will be displayed it is the engine), 
in the footer for example. Add ``{% include "instant/messages.html" %}`` where you want the message counter to be.
