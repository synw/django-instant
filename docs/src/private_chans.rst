Private channels
================

Authentication
~~~~~~~~~~~~~~

To use private channels add this in you main url file:

.. highlight:: python

::

   from instant.views import instant_auth
   
   urlpatterns = [
   	# ...
   	url(r'^centrifuge/auth/$', instant_auth, name='instant-auth'),
   	]

All the channels prefixed with a dollar sign **$** are considered private.

.. highlight:: python

::

   from instant.producers import publish 

   publish(message='Private event', channel="$private_chan")
   

Security
~~~~~~~~
   
All the messages sent to the Centrifugo server are signed using the secret key. 
When a client requests a connection to a private channels Centrifugo sends an ajax 
request to ``/centrifuge/auth/`` and expects to receive a signed response
that will indicate if the user is authorized or not.

More info `here <https://fzambia.gitbooks.io/centrifugal/content/mixed/private_channels.html>`_ about Centrifugo's auth
mechanism.