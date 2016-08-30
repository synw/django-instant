Client-side event handlers
==========================

You can customize the javascript that will handle each class of event. 

Create a template ``instant/extra_handlers.js`` with this content:

.. highlight:: django

::
   
   {% include "mymodule/handlers.js" %}
   
In ``templates/mymodule/handlers.js`` define your client side handler:

.. highlight:: javascript

::
   
	if (event_class == '__myeventclass__') {
		console.log(message);
		return false
	}
	
Return ``true`` if you want the default message to popup, ``false`` to disable the default behaviour.