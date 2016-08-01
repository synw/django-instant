{% include "instant/js/utils.js" %}

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
	return true
}