Send events
===========

Run the Centrifugo server:

.. highlight:: bash

::

   ./centrifugo --config=config.json --port=8001
   
Use the ``-d`` flag for debug. See the `Centrifugo config options <https://fzambia.gitbooks.io/centrifugal/content/server/configuration.html>`_.

There are two ways to publish events:

Stream events from code
~~~~~~~~~~~~~~~~~~~~~~~

.. highlight:: python

::

   from instant.producers import publish 

   # fire an event on the public channel
   publish(message='Hello world', event_class="infos", channel="public", data={"myfield":"my_value"})
   
   # send an instant debug message during development
   publish("Something happened somewhere in the code", event_class='debug')
   
The only required parameter is ``message``.

To send extra data pass some json into ``data``.

**Note**: if no channel is provided the events are published to the default public channel.

Direct publish of events
~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to ``/instant/`` as superuser and use the form to publish a message to a channel.

By default the sent messages pop up on the top-right corner of the page. The next section will describe how to 
customize the handlers on the client side according to the event class.
