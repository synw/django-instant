Client-side messages handlers
=============================

Default handler
---------------

The default messages handler is ``templates/instant/handlers/default.js``. Ex usage:

.. highlight:: javascript

::

   if (channel === "somechan") {
      console.log(message)
   } 

Channel handlers
----------------

Each channel can have its own javascript handler: create it in the handlers directory: 
example: if a ``$mychan`` is declared in settings create a 
``templates/instant/handlers/$mychan.js`` file to manage the handling logics
for that channel:

.. highlight:: javascript

::

   if (event_class === "someclass") {
      console.log(message)
   } 

Available javascript variables in handlers:

``event_class`` : class of the event

``channel`` : name of the channel

``message`` : text message

``data`` : json payload

``site`` : site slug

``uid`` : unique id of the message

``timestamp`` : date timestamp

Debug
-----

Note: for javascript debugging you can set a ``INSTANT_DEBUG = True`` in settings.py

Connection handler
------------------

To perform custom actions on connect and disconnect events create templates:

Template `instant/events/connect.js` or `instant/events/disconnect.js`:

.. highlight:: django

::
   
	{% include "myapp/myjs.js %}

This javascript will be executed on the selected event

