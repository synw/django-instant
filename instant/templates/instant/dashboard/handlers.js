{% load instant_tags %}
//console.log("NUM: {% num_excluded_chans %}");
{% if num_excluded_chans != 0 %}
	var exclude = [{% exclude_chans %}];
	//console.log("EX VAR: "+exclude);
	for (i=0;i<exclude.length;i++) {
		//console.log(channel+" / "+exclude[i]);
		if (event_class === exclude[i]) {
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
app.msgs.unshift({"event_class": event_class, "message": message, "uid": uid});
document.getElementById("instant_msgs").style.display = "inline-block";

//console.log("AUTOMSG", app.autoMsg);

if (app.autoMsg === true ) {
	if (app.sidebar === false) {
		app.toggleSidebar()
	}
}
app.numMsgs++;