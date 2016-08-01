// UI handlers
function hide_streambox() {
	$('#streambox-btns').hide();
	$('#streambox').hide();
}
function reset_counter() {
	$('#num_msgs').html('0');
	hide_streambox();
}
function clear_msgs() {
	$('.mqmsg').remove();
	$('#msgs_counter').hide();
	reset_counter();
}
function increment_counter() {
	var new_num = parseFloat($('#num_msgs').html())+1;
	$('#num_msgs').html(new_num);
	return new_num
}
function decrement_counter() {
	var num_msgs = parseFloat($('#num_msgs').html());
	var new_num = num_msgs - 1;
	if (new_num <= 0) {
		$('#msgs_counter').hide();
	}
	$('#num_msgs').html(new_num);
	return new_num
}
function delete_msg(msg) {
	msg.parentNode.remove();
	num_msgs = decrement_counter();
	if (num_msgs == 0) {
		hide_streambox();
	}
}
function format_data(message, event_class, label) { 
	return '<div class="mqmsg inbox '+event_class+'-msg"><a href="#" onclick="delete_msg(this)">'+label+'&nbsp;&nbsp;'+message+'</a>&nbsp;&nbsp;<a class="btn btn-default pull-right" style="background-color:lightgrey;position:relative;top:-0.5em" href="#" onclick="delete_msg(this)">OK</a></div>'
}