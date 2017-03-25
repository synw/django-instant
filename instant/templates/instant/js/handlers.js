{% load instant_tags %}

function handlers_for_event(event_class, channel, message, data, site, timestamp, uid) {
	/* ex: if ( channel == "{% get_public_channel %}" ) {
		console.log(message);
	}*/
	{% include "instant/extra_handlers.js" %}
}