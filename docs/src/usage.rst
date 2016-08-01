Usage
=====

Run the Centrifugo server:

.. highlight:: bash

::

   ./centrifugo --config=config.json
   
Use the ``-d`` flag for debug and a port if needed: ``--port=8008``.

**Note**: for now events can only be broadcasted to the site public channel. This means the messages sent
this way will be visible by everyone. A private channels implementation is on the todo list.

There is two ways to broadcast events:

Stream events from code
~~~~~~~~~~~~~~~~~~~~~~~ 

.. highlight:: python

::

   from instant import broadcast 

   # fire an event on the public channel
   instant.broadcast(message='Hello world', event_class="Infos")
   
The only required parameter is ``message``.

Direct broadcast of events
~~~~~~~~~~~~~~~~~~~~~~~~~~

Got to /instant/ as superuser and use the form to broadcast a message to the public channel.

By default the sent messages popup on the top-right corner of the page. The next section will describe how to 
customize the handlers on the client side according to the event class.
