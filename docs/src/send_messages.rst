Send messages
=============

To publish messages from python code:

.. highlight:: python

::

   from instant.producers import publish 

   # fire a message on the public channel whith error handling
   err = publish(message='Hello world', event_class="infos", 
                 channel="public", data={"myfield":"my_value"})
   if err != None:
      print("Error", str(err))
   
   # send an instant debug message during development
   publish("Something happened somewhere in the code", channel="$debug", 
           event_class='debug')
   
Required parameters: ``message`` and ``channel``

To send extra data pass some json into ``data``. Note: for now this won't work if you use 
the Go engine.

**Note**: if no channel is provided the events are published to the default public channel. 
This behavior is going to be deprecated as the public channel is going to be removed in future
versions so be sure to specify a channel.
