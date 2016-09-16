{% load instant_tags %}

var debug = {% debug_mode %};

{% include "instant/js/utils.js" %}

// websocket connection management
{% get_timestamp as timestamp %}
var centrifuge = new Centrifuge({
    url: "{% get_centrifugo_url %}",
    user: "{{ request.user.username }}",
    timestamp: "{{ timestamp }}",
    token: "{% mq_generate_token user.username timestamp %}"
});

var public_callbacks = {
    "message": function(dataset) {
    	//console.log('SET: '+JSON.stringify(dataset));
    	var channel = dataset['channel'];
    	var d = new Date();
    	var timestamp = new Date(dataset['timestamp']*1000 + d.getTimezoneOffset() * 60000);
    	res = unpack_data(dataset);
    	var message = res['message']
    	var event_class = res['event_class']
    	var message_label = res['message_label']
    	var data = res['data']
    	var channel = res['channel'];
    	var site = res['site'];
    	if ( debug === true ) {
    		console.log('Msg: '+message+"\nChan: "+channel+"\nEvent_class: "+event_class+'\nData: '+JSON.stringify(data));
    	}
    	var alert_on_event = handlers_for_event(event_class, channel, message, data, site, timestamp);
		if (alert_on_event === true ) {
			// default behavior: popup a message on the top right corner
			$('#streambox').prepend(format_data(message, event_class, message_label));
			num_msgs = increment_counter();
			if (num_msgs > 0) {
		    	$('#msgs_counter').show();
		    	$('#streambox').show();
		    	$('#streambox').delay(15000).fadeOut();
			}
		};
    },
    {% include "instant/js/join_events.js" %}
}

var subscription = centrifuge.subscribe("{% get_public_channel %}", public_callbacks);

centrifuge.on('connect', function(context) {
	if ( debug === true ) {console.log("Connection ("+context.latency+"ms)")};
});

centrifuge.on('disconnect', function(context) {
	if ( debug === true ) {console.log("Disconnection: "+context.reason)};
});

{% include "instant/extra_clients.js" %}

{% is_superuser_channel as enable_superuser_channel %}
{% if enable_superuser_channel %}
	{% if user.is_superuser %}
		{% include "instant/channels/superuser/client.js" %}
	{% endif %}
{% endif %}

{% is_staff_channel as enable_staff_channel %}
{% if enable_staff_channel %}
	{% if user.is_staff %}
		{% include "instant/channels/staff/client.js" %}
	{% endif %}
{% endif %}

{% is_users_channel as enable_users_channel %}
{% if enable_users_channel %}
	{% if user.is_authenticated %}
		{% include "instant/channels/users/client.js" %}
	{% endif %}
{% endif %}

centrifuge.connect();