{% load instant_tags %}

var mq_callbacks_{% get_users_channel %} = {
    "message": function(dataset) {
    	if (debug === true) { console.log('DATASET: '+JSON.stringify(dataset));};
    	res = unpack_data(dataset);
    	var message = res['message']
    	var event_class = res['event_class']
    	var message_label = res['message_label']
    	var data = res['data']
    	var channel = res['channel'];
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
    	//var site = res['site'];
    	//if ( site != "" ) {
    	//	var output ='<div class="pull-right badge" style="margin-left:0.5em;font-size:85%">'+site+'</div>';
    	//}
    	output = output+'<div style="margin:1.2em;">'+timenow+' '+message_label+'&nbsp;&nbsp;'+message+'</div>';
    	$('#user_msgs').prepend(output);
    },
    {% include "instant/js/join_events.js" %}
}

var subscription = centrifuge.subscribe("{% get_users_channel %}", mq_callbacks_{% get_users_channel %});