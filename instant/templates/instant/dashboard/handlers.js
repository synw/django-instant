{% load vvinstant_tags %}
//console.log("NUM: {% num_excluded_chans %}");
{% if num_excluded_chans != 0 %}
	var exclude = [{% exclude_chans %}];
	//console.log("EX VAR: "+exclude);
	for (i=0;i<exclude.length;i++) {
		console.log(channel+" / "+exclude[i]);
		if (channel === exclude[i]) {
			return
		}
	}
{% else %}
//console.log("NO");
{% endif %}
app.msgIconClass["fa-envelope-o"] = false;
app.msgIconClass["fa-envelope"] = true;
setTimeout(function(){
	app.msgIconClass["fa-envelope-o"] = true;
	app.msgIconClass["fa-envelope"] = false;
},1200);
if ( event_class == 'important' ) {
	app.warningMsg = message;
	$("#warning-msg").slideDown();
} else if ( event_class == 'info' ) {
	app.infoMsg = message;
	$("#info-msg").slideDown();
	setTimeout(function() {$("#info-msg").slideUp()}, 5000);
} else {
	app.numMsgs++;
	app.msgs.unshift({"event_class": event_class, "message": message, "uid": uid});
	document.getElementById("instant_msgs").style.display = "inline-block";
	if (app.autoMsg === true ) {
		if (app.showSidebar === false) {
			app.toggleSidebar()
		}
	}
}