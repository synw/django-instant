{% load instant_tags %}

function handlers_for_{{ chan_name }}(event_class, channel, message, data, site, uid, timestamp) {
	{% if handler_template %}
		{% include handler_template %}
	{% else %}
		{% if handler %}
			{{ handler }}
		{% else %}
			handlers_for_event(event_class, channel, message, data, site, uid, timestamp);
		{% endif %}
	{% endif %}
}

var {{ chan_name }}_callbacks = {
    "message": function(dataset) {
    	if (instantDebug === true) { console.log('DATASET from {{ chan }}: '+JSON.stringify(dataset));};
    	payload = dataset;
    	{% if deserializer_template %}
    		res = (function(payload) { {% include deserializer_template %} })(payload);
    	{% else %}
	    	{% if deserializer %}
		    	res = (function(payload) { {{deserializer}} })(payload);
	    	{% else %}
	    		res = unpack_data(dataset);
	    	{% endif %}
    	{% endif %}
    	var message = res['message'];
    	var event_class = res['event_class'];
    	var message_label = res['message_label'];
    	var data = res['data'];
    	var channel = res['channel'];
    	var uid = res['UID'];
    	var site = res["site"];
    	var timestamp = res['timestamp']
    	// handlers
    	if (instantDebug === true) {
			console.log('Msg:', message,
					"Chan: ", channel,
					"Event_class: ", event_class,
					"Data: ", JSON.stringify(data, null, 2)
			);
    	}
    	{% if request.path|slice:'8' == "/instant" %}
    		handlers_for_event(event_class, channel, message, data, site, uid, timestamp);
    	{% else %}
    		handlers_for_{{ chan_name }}(event_class, channel, message, data, site, uid, timestamp);
    	{% endif %}
    },
    {% include "instant/js/join_events.js" %}
}

var {{ chan_name }}_subscription = centrifuge.subscribe("{{ chan }}", {{ chan_name }}_callbacks);