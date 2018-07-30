Custom channels
===============

Custom javascript client
~~~~~~~~~~~~~~~~~~~~~~~~

Create a ``{% instant/extra_clients.js %}`` template that contains something like:

.. highlight:: django

::
   
   {% if user.is_authenticated and request.path == "/private/" %}
   	{% include "myapp/client.js" %}
   {% endif %}

Edit ``myapp/client.js``:

.. highlight:: django

::
   
   var my_callbacks = {
      "message": function(dataset) {
      // the instantDebug variable is set via INSTANT_DEBUG = True in settings.py
      if (instantDebug === true) { console.log('EVENT: '+JSON.stringify(dataset));};
      res = unpack_data(dataset);
      var message = res['message']
      var event_class = res['event_class']
      var message_label = res['message_label']
      var data = res['data']
      var channel = res['channel'];
      if ( data.hasOwnProperty('my_field) ) {
       my_field = data['myfield']
      }
      // do something with the data
      console.log(message);
   },
   {% include "instant/js/join_events.js" %}
     
   var subscription = centrifuge.subscribe("$mychannel", my_callbacks);

   
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
   from instant.utils import signed_response
   
   @csrf_exempt
   def mychan_auth_view(request):
       if not request.is_ajax() or not request.method == "POST":
           raise Http404
       data = json.loads(request.body)
       channels = data["channels"]
       client = data['client']
       response = {}
       for channel in channels:
       	   response[channel] = {"status","403"}
           if channel == "$mychannel":
           	# checks come here	
           	if request.user.is_authenticated() and whatever():
           	   response[channel] = signed_response(channel, client) 
       return JsonResponse(response)
	    



