Database channels
=================

**New in 0.7** to come

A ``Channel`` model is available to create channels. Fields:

:**slug**: the channel name
:**role**: the authorization level for the channel: public, users, groups, staff or superuser
:**active**: a boolean to activate or not the channel
:**groups**: group objects that can connect to the channel
:**paths**: paths where to connect the channel
:**handler_template**: template url for the javascript handler
:**handler**: javascript handler code
:**deserializer_template**: template url for the javascript deserializer
:**deserializer**: javascript deserializer code

Create channels
~~~~~~~~~~~~~~~

The channels are created like any other model in the admin or in the code:

.. highlight:: python

::

   from instant.models import Channel
   
   Channel.objects.get_or_create(
            slug="$myPrivateChan",
            role="superuser",
            paths="/somewhere,/somewhere/else")
            
If paths are provided the channel will connect only on these urls, otherwise it will
connect everywhere.

*Note*: once the channels are created all the related information is stored in memory, so
that when the channels connect or when the backend authenticates a user no query is made
   
Handlers
~~~~~~~~

There are two ways to define custom javascript handlers for a channel:

**1. In a template**: if the ``handler_template`` field is used the template at the provided url
will be loaded. 

Example: a ``mymodule/handlers.js`` value will load the ``templates/mymodule/handlers.js`` template
to handle the messages for the channel in javascript.

**2. In the handlers field**: write your handler function directly in the field. 
Example ``handler`` value:

.. highlight:: javascript

::

   console.log(message)

Available javascript variables for handler functions:

``event_class`` : class of the event

``channel`` : name of the channel

``message`` : text message

``data`` : json payload

``site`` : site slug

``uid`` : unique id of the message

``timestamp`` : date timestamp

Deserializers
~~~~~~~~~~~~~

Custom deserializers can be used with the ``deserializer`` and ``deserializer_template`` fields. It is
a function body that have to return the above variables in a ``data`` dictionnary.

Example:

.. highlight:: javascript

::

   data = {
	"UID": payload.data.Id,
	"message": payload.data.ReturnValues.join(" "),
	"timestamp": payload.data.Date,
	"channel": payload.channel,
	"event_class": "Command",
	"data": {}
	}
	return data
