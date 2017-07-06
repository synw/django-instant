{% load instant_tags %}

function handlers_for_event(event_class, channel, message, data, site, uid) {
	/* ex: if ( channel == "{% get_public_channel %}" ) {
		console.log(message);
	}*/
	{% if user.is_superuser %}
		{% if request.path|slice:8 == "/instant" %}
			{% include "instant/frontend/handlers.js" %}
		{% endif %}
	{% endif %}
	{% include "instant/extra_handlers.js" %}
}