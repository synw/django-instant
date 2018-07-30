.. django-instant documentation master file, created by
   sphinx-quickstart on Mon Aug  1 12:48:52 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Django Instant's documentation
==============================

Instant delivers events in real time to the userland using the 
`Centrifugo <https://github.com/centrifugal/centrifugo/>`_  websockets server.

.. toctree::
	:maxdepth: 2
	:caption: Install
   
	src/install
	
.. toctree::
	:maxdepth: 2
	:caption: Create channels
   
	src/declarative_chans
	src/default_chans

.. toctree::
	:maxdepth: 2
	:caption: Handle messages
   
	src/send_messages
	src/handle_messages
	src/formating
	
.. toctree::
	:maxdepth: 2
	:caption: Security
	
	src/private_chans
	src/custom_chans

	


