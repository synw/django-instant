Create channels
===============

*New in 0.6 - still experimental*: declarative channels

Declare channels
~~~~~~~~~~~~~~~~

To declare new channels in settings.py use this format:

.. highlight:: python

::

   ["channel_name", ["/path/where/to/connect/it"]]
   
   
If the second element of the tuple is set the channels will be connected only for the listed path. If not set
the channel will autoconnect on every path. Example:

.. highlight:: python

::

   INSTANT_SUPERUSER_CHANNELS = [
    ["$mysite_admin1", ["/a/path", "/another/path"]]
    ['$mysite_admin2']
   )
   INSTANT_STAFF_CHANNELS = [
    ["$mysite_staff1", ["/a/path"]]
    ['$mysite_staff2',),
   ]
   INSTANT_USERS_CHANNELS = [
    ['$mysite_users1']
   ]
   INSTANT_PUBLIC_CHANNELS = [
    ['mysite_public1']
    ['mysite_public2']
   ]
   
Note: be sure to configure auth if you use private channels: see private channels section for instructions.
   
Handlers
~~~~~~~~

You can create a ``/templates/instant/handlers/default.js`` file that will be the default handler for
the channels.

Each channel can have its own handler: just create it in the handlers directory: example: if a ``$mychan`` is declared in
settings it is possible to create a ``$mychan.js`` file in the handlers directory to manage the handling logics 
just for that channel.

Example handler:

.. highlight:: javascript

::

   if (event_class === "someclass") {
      console.log(message)
   } 

Available variables:

``event_class`` : class of the event

``channel`` : name of the channel

``message`` : text message

``data`` : json payload

``site`` : site slug

``uid`` : unique id of the message

``timestamp`` : date timestamp
