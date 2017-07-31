Send events
===========

Run the websockets server:

.. highlight:: bash

::

   python3 manage.py runws
   
There are two ways to publish events:

Direct publish of events
~~~~~~~~~~~~~~~~~~~~~~~~

Go to ``/instant/`` as superuser and use the form to publish a message to a channel.

The next section will describe how to 
customize the handlers on the client side according to the event class.

Stream events from code
~~~~~~~~~~~~~~~~~~~~~~~

.. highlight:: python

::

   from instant.producers import publish 

   # fire an event on the public channel whith error handling
   err = publish(message='Hello world', event_class="infos", channel="public", data={"myfield":"my_value"})
   if err != None:
      print("Error", str(err))
   
   # send an instant debug message during development
   publish("Something happened somewhere in the code", event_class='debug')
   
The only required parameter is ``message``.

To send extra data pass some json into ``data``.

**Note**: if no channel is provided the events are published to the default public channel.
