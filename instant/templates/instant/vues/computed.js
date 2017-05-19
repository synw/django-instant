showMsgsCounter: {
	get: function () {
		if ( this.numMsgs > 0 ) {
			return "block"
		}
		return "none"
	},
	set: function () {
		if ( this.numMsgs > 0 ) {
			return "block"
		}
		return "none"
	}
},