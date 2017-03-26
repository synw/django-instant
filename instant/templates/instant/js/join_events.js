"join": function(message) {
	if ( instantDebug === true ) {console.log('JOIN: '+JSON.stringify(message))};
},
"leave": function(message) {
	if ( instantDebug === true ) {console.log('LEAVE: '+JSON.stringify(message))};
},
"subscribe": function(context) {
	if ( instantDebug === true ) {console.log('SUSCRIBE: '+JSON.stringify(context))};
},
"error": function(errContext) {
	if ( instantDebug === true ) {console.log('ERROR: '+JSON.stringify(errContext))};
},
"unsubscribe": function(context) {
	if ( instantDebug === true ) {console.log('UNSUSCRIBE: '+JSON.stringify(context))};
}