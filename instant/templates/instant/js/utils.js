function getClockTime(seconds) {
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