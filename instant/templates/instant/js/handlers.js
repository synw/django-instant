{% load instant_tags %}

{% include "instant/js/utils.js" %}

function handlers_for_event(event_class, channel, message, data, timestamp) {
	// return true if we want the regular alert to be displayed, false otherwise
	if ( channel == "{% get_public_channel %}" ) {
		if (event_class == 'Minor') {
			$('#minorbox').show(0).delay(1000).hide(0);
			return false
		}
		if (event_class == 'Important') {
			playSound();
			return true
		}
		if (event_class == 'Announce') {
			$('#jumbocontent').prepend(message);
			$('#jumbobox').css('display','table-cell');
			return false
		}
	}
	{% include "instant/extra_handlers.js" %}
	return true
}