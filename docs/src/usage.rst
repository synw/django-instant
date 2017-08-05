Send messages
=============
   
There are two ways to publish messages:

Direct publish of messages
~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to ``/instant/`` as superuser and use the form to publish a message to a channel.

The next section will describe how to 
customize the handlers on the client side according to the event class.

Stream messages from code
~~~~~~~~~~~~~~~~~~~~~~~~~

.. highlight:: python

::

   from instant.producers import publish 

   # fire a message on the public channel whith error handling
   err = publish(message='Hello world', event_class="infos", channel="public", data={"myfield":"my_value"})
   if err != None:
      print("Error", str(err))
   
   # send an instant debug message during development
   publish("Something happened somewhere in the code", event_class='debug')
   
The only required parameter is ``message``.

To send extra data pass some json into ``data``.

**Note**: if no channel is provided the events are published to the default public channel.
