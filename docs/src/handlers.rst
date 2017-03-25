Client-side event handlers
==========================

You can customize the javascript that will handle each class of event of the default public channel. 

Create a template ``instant/extra_handlers.js`` with this content:

.. highlight:: django

::
   
   {% include "mymodule/handlers.js" %}
   
In ``templates/mymodule/handlers.js`` define your client side handler:

.. highlight:: javascript

::
   
	if ( event_class == 'anyeventclass' ) {
		console.log(message);
	}

Note: for javascript debugging you can set a ``INSTANT_DEBUG = True`` in settings.py

Note: this is only available for the default public channel events. To handle events in private channels
see next section.

Message label formating
-----------------------

The default behavior pops up a message with a label according to the event_class. To change these default
labels use the file ``templates/instant/event_class_format.js``.

The default css classes are defined in ``instant/static/instant.css``:

.. highlight:: javascript

::
   
   {
   'default' : 'mq-label mq-default',
   'important' : 'mq-label mq-important',
   'ok' : 'mq-label mq-ok',
   'info' : 'mq-label mq-info',
   'debug' : 'mq-label mq-debug',
   'warning' : 'mq-label mq-warning',
   'error' : 'mq-label mq-error',
   'object created' : 'mq-label mq-created',
   'object edited' : 'mq-label mq-edited',
   'object deleted' : 'mq-label mq-deleted',
   }

Default icons (using font-awesome):

.. highlight:: javascript

::
   
   {
   'default' : '<i class="fa fa-flash"></i>',
   'important' : '<i class="fa fa-exclamation"></i>',
   'ok' : '<i class="fa fa-thumbs-up"></i>',
   'info' : '<i class="fa fa-info-circle"></i>',
   'debug' : '<i class="fa fa-cog"></i>',
   'warning' : '<i class="fa fa-exclamation"></i>',
   'error' : '<i class="fa fa-exclamation-triangle"></i>',
   'object edited' : '<i class="fa fa-pencil"></i>',
   'object created' : '<i class="fa fa-plus"></i>',
   'object deleted' : '<i class="fa fa-remove"></i>',
   }
 