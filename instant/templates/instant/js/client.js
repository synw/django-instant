{% load instant_tags %}

var instantDebug = {% debug_mode %};

{% include "instant/js/utils.js" %}

{% get_timestamp as timestamp %}
var centrifuge = new Centrifuge({
	url: "{% get_centrifugo_url %}",
    user: "{% if user.is_anonymous %}anonymous{% else %}{{ request.user.username }}{% endif %}",
    timestamp: "{{ timestamp }}",
    token: "{% if user.is_anonymous %}{% mq_generate_token 'anonymous' timestamp %}{% else %}{% mq_generate_token user.username timestamp %}{% endif %}"
});

{% public_channel_is_on as enable_public_channel %}
{% if enable_public_channel %}
var public_callbacks = {
    "message": function(dataset) {
    	var channel = dataset['channel'];
    	var d = new Date();
    	res = unpack_data(dataset);
    	var message = res['message'];
    	var event_class = res['event_class'];
    	var message_label = res['message_label'];
    	var data = res['data'];
    	var channel = res['channel'];
    	var uid = res['uid'];
    	var site = res['site'];
    	if (instantDebug === true && event_class !== "__presence__") { console.log('DATASET: '+JSON.stringify(dataset)) };
    	handlers_for_event(event_class, channel, message, data, site, uid);
    },
    {% include "instant/js/join_events.js" %}
}

var public_subscription = centrifuge.subscribe("{% get_public_channel %}", public_callbacks);

centrifuge.on('connect', function(context) {
	if ( instantDebug === true ) {console.log("Connection ("+context.latency+"ms)")};
	{% include "instant/events/connect.js" %}
});

centrifuge.on('disconnect', function(context) {
	if ( instantDebug === true ) {console.log("Disconnection: "+context.reason)};
	{% include "instant/events/disconnect.js" %}
});
{% endif %}

{% include "instant/extra_clients.js" %}

{% if user.is_superuser %}
	{% is_superuser_channel as enable_superuser_channel %}
	{% if enable_superuser_channel %}
		{% include "instant/channels/superuser/client.js" %}
	{% endif %}
	{% get_superuser_channels as supchans %}
	{% for chan in supchans %}
		{% get_handlers_url chan as handlers %}
		{% with handlers.0 as url %}
		{% with handlers.1 as chan_name %}
			{% include "instant/channels/client.js" %}
		{% endwith %}
		{% endwith %}
	{% endfor %}
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