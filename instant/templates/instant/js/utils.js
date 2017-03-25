function getClockTime(seconds)
{
   var now    = new Date();
   var hour   = now.getHours();
   var minute = now.getMinutes();
   var second = now.getSeconds();
   if (hour   > 12) { hour = hour - 12;      }
   if (hour   == 0) { hour = 12;             }
   if (hour   < 10) { hour   = "0" + hour;   }
   if (minute < 10) { minute = "0" + minute; }
   if (seconds == true && second < 10) { second = "0" + second; }
   var timestring = hour +':' +minute;
   if (seconds == true) {
	   timestring = timestring+':'+second;
   }
   return timestring;
}

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
	return res
}