"join": function(message) {
	if ( debug === true ) {console.log('JOIN: '+JSON.stringify(message))};
},
"leave": function(message) {
	if ( debug === true ) {console.log('LEAVE: '+JSON.stringify(message))};
},
"subscribe": function(context) {
	if ( debug === true ) {console.log('SUSCRIBE: '+JSON.stringify(context))};
},
"error": function(errContext) {
	if ( debug === true ) {console.log('ERROR: '+JSON.stringify(errContext))};
},
"unsubscribe": function(context) {
	if ( debug === true ) {console.log('UNSUSCRIBE: '+JSON.stringify(context))};
}