Usage
=====

Run the Centrifugo server:

.. highlight:: bash

::

   ./centrifugo --config=config.json
   
Use the ``-d`` flag for debug and a port if needed: ``--port=8001``.

**Note**: for now events can only be broadcasted to the site public channel. This means that the messages sent
this way might be visible by everyone. Do not use for private data.
A private channels implementation is on the todo list.

There are two ways to broadcast events:

Stream events from code
~~~~~~~~~~~~~~~~~~~~~~~ 

.. highlight:: python

::

   from instant import broadcast 

   # fire an event on the public channel
   instant.broadcast(message='Hello world', event_class="infos")
   
   # send an instant debug message during development
   broadcast("Something happened somewhere in the code", event_class='debug')
   
The only required parameter is ``message``.

Direct broadcast of events
~~~~~~~~~~~~~~~~~~~~~~~~~~

Got to /instant/ as superuser and use the form to broadcast a message to the public channel.

By default the sent messages pops up on the top-right corner of the page. The next section will describe how to 
customize the handlers on the client side according to the event class.
