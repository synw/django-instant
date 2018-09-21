formMsg: function() {
	btn = this.get("post-btn");
	if (this.formMsg.length>0) {
		btn.disabled = false;
	} else {
		btn.disabled = true;
	}
},