{% load instant %}

var debug = false;

// websocket connection management
{% get_timestamp as timestamp %}
var centrifuge = new Centrifuge({
    url: "{% get_centrifugo_url %}",
    user: "{{ request.user.username }}",
    timestamp: "{{ timestamp }}",
    token: "{% mq_generate_token user.username timestamp %}"
});

var public_callbacks = {
    "message": function(message) {
        var msg = message.data.message;
        var channel = message.channel;
        var event_class = message.data.event_class
        var message_label = message.data.message_label;
        if ( debug === true ) {
        	console.log('MESSAGE: '+msg+'\nChannel: '+channel+'\nEvent class: '+event_class+'\nLabel: '+message_label);
        }
        var alert_on_event = handlers_for_event_class(event_class, channel, msg);
		if (alert_on_event === true) {
			// default behavior: popup a message on the top right corner
			$('#streambox').prepend(format_data(msg, event_class, message_label));
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
    	if ( debug === true ) {console.log('ERROR: '+JSON.stringify(err))};
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
{% get_apps as apps %}
{% if "presence" in apps %}
	subscription.presence().then(function(message) {
		if ( debug === true ) {console.log('PRESENCE: '+JSON.stringify(message.data))};
	}, function(err) {
		if ( debug === true ) {console.log('PRESENCE ERROR: '+err)};
	});
{% endif %}

centrifuge.connect();