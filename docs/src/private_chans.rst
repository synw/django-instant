Private channels
================

To send a message to a private channel use a **$** sign to prefix the channel name:

.. highlight:: python

::

   from instant import broadcast 

   broadcast(message='Private event', channel="$private_chan")
   

Security
~~~~~~~~
   
All the messages sent to the Centrifugo server are signed using the secret key. When a client requests a connection to
a private channels Centrifugo sends an ajax request to ``/centrifugo/auth/`` and expects to receive a signed response
that will indicate if the user is authorized or not.

You will need to implement a function in your backend to authenticate the user. Example: urls.py:

.. highlight:: python

::

   from mymodule.views import mychan_auth_view
   url(r'^centrifuge/auth/$', mychan_auth_view),
   
In views.py:

.. highlight:: python

::

   from django.views.decorators.csrf import csrf_exempt
   from django.http.response import Http404
   from cent.core import generate_channel_sign
   from instant.conf import SECRET_KEY
	
   @csrf_exempt
   def mqueue_livefeed_auth(request):
       if not request.is_ajax() or not request.method == "POST":
           raise Http404
       data = json.loads(request.body)
       channels = data["channels"]
       client = data['client']
       channel = channels[0]
       payload = {channel:{"status",403}}
       if request.user.is_superuser:
           signature = generate_channel_sign(SECRET_KEY, client, channel, info="")
           payload = {channel:{"sign": signature}}
       return JsonResponse(payload)
	    

More info `here <https://fzambia.gitbooks.io/centrifugal/content/mixed/private_channels.html>`_ about Centrifugo's auth
mechanism.

	    