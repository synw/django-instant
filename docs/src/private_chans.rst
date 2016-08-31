Private channels
================

All the channels prefixed with a dolar sign **$** are considered private.

.. highlight:: python

::

   from instant import broadcast 

   broadcast(message='Private event', channel="$private_chan")
   

Security
~~~~~~~~
   
All the messages sent to the Centrifugo server are signed using the secret key. When a client requests a connection to
a private channels Centrifugo sends an ajax request to ``/centrifugo/auth/`` and expects to receive a signed response
that will indicate if the user is authorized or not.

More info `here <https://fzambia.gitbooks.io/centrifugal/content/mixed/private_channels.html>`_ about Centrifugo's auth
mechanism.

Using Instant auth
~~~~~~~~~~~~~~~~~~

In you main url file:

.. highlight:: python

::

   from instant.views import instant_auth
   
   urlpatterns = [
   	# ...
   	url(r'^centrifuge/auth/$', instant_auth, name='instant-auth'),
   	]

Set you channels credentials in settings.py:

.. highlight:: python

::

   # logged in users only: if not set default is SITE_SLUG+'_users'
   INSTANT_USERS_CHANNELS = ['$userschan']
   # staff only: if not set default is SITE_SLUG+'_staff'
   INSTANT_STAFF_CHANNELS = ['$staffchan']
   # superusers only: if not set default is SITE_SLUG+'_admin'
   INSTANT_SUPERUSER_CHANNELS = ['$adminchan']
   
   
Custom auth function
~~~~~~~~~~~~~~~~~~~~

You can write a custom auth backend to authenticate the user. Example: urls.py:

.. highlight:: python

::

   from mymodule.views import mychan_auth_view
   url(r'^centrifuge/auth/$', mychan_auth_view),
   
In views.py:

.. highlight:: python

::

   import json
   from django.http import JsonResponse
   from django.views.decorators.csrf import csrf_exempt
   from django.http.response import Http404
   from cent.core import generate_channel_sign
   from instant.conf import SECRET_KEY
	
   def signed_response(channel, client):
    signature = generate_channel_sign(SECRET_KEY, client, channel, info="")
    return {"sign": signature}

   @csrf_exempt
   def instant_auth(request):
       if not request.is_ajax() or not request.method == "POST":
           raise Http404
       data = json.loads(request.body)
       channels = data["channels"]
       client = data['client']
       response = {}
       for channel in channels:
       	   response[channel] = {"status","403"}
           if channel == "$channel_to_check":
           	# checks come here	
           	if request.user.is_authenticated() and whatever():
           		signature = signed_response(channel, client)
           		response[channel] = signature   
       return JsonResponse(response)
	    



	    