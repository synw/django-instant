{% load instant %}
{% include "instant/js/utils.js" %}
{% get_apps as apps %}
{% if "presence" in apps %}
	{% include "presence/js/utils.js" %}
{% endif %}

function handlers_for_event_class(event_class, channel, message) {
	// return true if we want the regular alert to be displayed, false otherwise
	if (event_class == 'Minor') {
		console.log(message);
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
	{% if "presence" in apps %}
		{% include "presence/js/handlers.js" %}
	{% else %}
		if (event_class == '__presence__') {
			return false
		}
	{% endif %}
	return true
}