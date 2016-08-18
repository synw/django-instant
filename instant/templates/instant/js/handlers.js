{% load instant_tags %}

{% include "instant/js/utils.js" %}
{% if "presence"|is_in_apps %}
	{% include "presence/js/utils.js" %}
{% endif %}

function handlers_for_event(event_class, channel, message, data, timestamp) {
	// return true if we want the regular alert to be displayed, false otherwise
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
	// presence app
	{% if "presence"|is_in_apps %}
		{% include "presence/js/handlers.js" %}
	{% else %}
		if (event_class == '__presence__') {
			return false
		}
	{% endif %}
	// rechat app
	{% if "rechat"|is_in_apps %}
		{% include "rechat/js/handlers.js" %}
	{% endif %}
	return true
}