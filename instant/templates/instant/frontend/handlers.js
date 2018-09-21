function get_channel(slug) {
	if (slug in app.publicChans === true) {
		return app.publicChans[slug]
	} else if (slug in app.usersChans === true) {
		return app.usersChans[slug]
	} else if (slug in app.staffChans === true) {
		return app.staffChans[slug]
	} else if (slug in app.superuserChans === true) {
		return app.superuserChans[slug]
	}
}
var now = getClockTime(true);
if (app.labels.indexOf(event_class) !== -1) {
	event_class=get_label(event_class);
};
var msg = {"time":now, "class": event_class, "channel": channel, "message": message, "data": app.str(data)};
$('#msgsTable').DataTable().row.add(msg).draw();
var chan = get_channel(channel);
app.msgReceived(chan);