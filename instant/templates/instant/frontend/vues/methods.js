activateForm: function(chan) {
	this.showForm = true;
	this.formChan = chan;
},
postInstantForm: function() {
	function error(err) {
        app.errorMsg("Client error posting the message: "+err.toString());
	}
	function action(response) {
		if (response.data.error !== 0) {
			var msg = 'Server error: '+response.data.error;
			app.errorMsg(msg);
		}
	}
	var url = "/instant/post/";
	this.postForm(url, "instant_form", action, error);
	this.formPosted();
},
formPosted: function() {
	this.showForm = false;
	this.formMsg = "";
	this.msgClass = "";
	this.formData = "";
    this.$toast.open({
        message: 'Message sent',
        type: 'is-success'
    })
},
drawSparkline: function() {
	var opts = { type:'line', fillColor:false, lineColor:"#3B3B3B", height:"2em" };
    $('.numMsgsSparkline').sparkline(app.timelineNumMsgs, opts);
},
getEventLabels: function() {
	var event_classes = this.labels;
	for (i=0;i<event_classes.length;i++) {
		this.eventLabels.push( {"name":event_classes[i], "label":get_label(event_classes[i])} );
	}
},
setEventLabel: function(label) {
	this.msgClass = label;
},
msgReceived: function(chan) {
	chan.msgs = chan.msgs+1;
	chan.isActive = false;
	chan.receiving = true;
	setTimeout(function() {
		chan.receiving = false;
		chan.isActive = true;
	}, 1000);
	this.timeframeMsgs++;
	this.timelineNumMsgs.push(this.timeframeMsgs);
},
errorMsg: function(msg) {
	this.showForm = false;
	this.$snackbar.open({
        message: msg,
        type: 'is-danger',
        position: 'is-top',
        actionText: 'Ok',
        indefinite: true,
    })
},