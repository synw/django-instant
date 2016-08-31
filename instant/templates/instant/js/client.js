{% load instant_tags %}

var debug = {% debug_mode %};

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
    	var message = "";
    	if (dataset['data'].hasOwnProperty('message')) {
    		var message = dataset['data']['message'];
    	}
    	var message_label = "";
    	if (dataset['data'].hasOwnProperty('message_label')) {
    		var message_label = dataset['data']['message_label'];
    	}
    	var event_class = "";
    	if (dataset['data'].hasOwnProperty('event_class')) {
    		var event_class = dataset['data']['event_class'];
    	}
    	var data = "";
    	if (dataset['data'].hasOwnProperty('data')) {
    		var data = dataset['data']['data'];
    	}
    	//console.log('Msg: '+message+"\nChan: "+channel+"\nEvent_class: "+event_class+'\nData: '+JSON.stringify(data));
        var alert_on_event = handlers_for_event(event_class, channel, message, data, timestamp);
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
    "join": function(message) {
    	if ( debug === true ) {console.log('JOIN: '+JSON.stringify(message))};
    },
    "leave": function(message) {
    	if ( debug === true ) {console.log('LEAVE: '+JSON.stringify(message))};
    },
    "subscribe": function(context) {
    	if ( debug === true ) {console.log('SUSCRIBE: '+JSON.stringify(context))};
    },
    "error": function(errContext) {
    	if ( debug === true ) {console.log('ERROR: '+JSON.stringify(errContext))};
    },
    "unsubscribe": function(context) {
    	if ( debug === true ) {console.log('UNSUSCRIBE: '+JSON.stringify(context))};
    }
}

var subscription = centrifuge.subscribe("{% get_public_channel %}", public_callbacks);

centrifuge.on('connect', function(context) {
	if ( debug === true ) {console.log("Connection ("+context.latency+"ms)")};
});

centrifuge.on('disconnect', function(context) {
	if ( debug === true ) {console.log("Disconnection: "+context.reason)};
});

{% include "instant/extra_clients.js" %}

centrifuge.connect();