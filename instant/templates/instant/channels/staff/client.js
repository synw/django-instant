{% load instant_tags %}

var staff_callbacks_{% get_staff_channel %} = {
    "message": function(dataset) {
    	if (debug === true) { console.log('DATASET: '+JSON.stringify(dataset));};
    	res = unpack_data(dataset);
    	var message = res['message']
    	var event_class = res['event_class']
    	var message_label = res['message_label']
    	var data = res['data']
    	var channel = res['channel'];
    	var site = res['site'];
    	var timestamp = res['timestamp'];
    	var d = new Date();
    	// handlers
    	if (debug === true) {
    			console.log('Msg: '+message+"\nChan: "+channel+"\nEvent_class: "+event_class+'\nData: '+JSON.stringify(data));
    	}
    	var timenow = getClockTime(false);
    	if ( data.hasOwnProperty('admin_url') ) {
    		message = '<a href="'+data['admin_url']+'" target="_blank">'+message+'</a>';
    	}
    	var output = "";
    	var alert_on_event = handlers_for_event(event_class, channel, message, data, site, timestamp);
		if (alert_on_event === true ) {
			output = output+'<div class="mq_message">'+timenow+' '+message_label+'&nbsp;&nbsp;'+message+'</div>';
    		$('#staff_msgs').prepend(output);
		}
    },
    {% include "instant/js/join_events.js" %}
}

var subscription = centrifuge.subscribe("{% get_staff_channel %}", staff_callbacks_{% get_staff_channel %});