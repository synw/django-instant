Client-side event handlers
==========================

You can customize the javascript that will handle each class of event. Use the template 
``instant/js/handlers.js`` and add your own event handler in the function:

.. highlight:: javascript

::
   
   function handlers_for_event_class(event_class, channel, message) {
	// return true if we want the regular alert to be displayed, false otherwise
	if (event_class == 'Important') {
		// do whatever you want
		alert('The message '+message+' is important');
		return false
	}
	return true
   }