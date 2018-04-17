function unpack_data(dataset) {
	var channel = dataset['channel'];
	var uid = dataset['uid'];
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
	var site = "";
	if (dataset['data'].hasOwnProperty('site')) {
		var site = dataset['data']['site'];
	}
	var res = {"channel":channel, "message": message, "event_class": event_class, "message_label": message_label, "data": data, "site":site, "uid": uid}
	console.log("UNPACK", res);
	return res
}