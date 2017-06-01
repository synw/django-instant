{% load i18n instant_tags %}
{% if user.is_superuser %}
	toggleInstantForm: function(){
		if (this.instantForm === true) {
			this.instantForm = false;
		} else {
			this.instantForm = true;
		}
	},
	postInstantForm: function() {
		var form = this.get("instant_form");
		var data = this.serializeForm(form);
		var empty = '<i class="fa fa-close" style="color:red"></i>&nbsp;{% trans "Please write a message" %}';
		var emptychan = '<i class="fa fa-close" style="color:red"></i>&nbsp;{% trans "Please select a channel" %}';
		if (data.msg === "") {
			this.statusMsg(empty);
			return
		}
		if (app.activeChannel === "") {
			this.statusMsg(emptychan);
			return
		}
		data["channel"] = this.activeChannel;
		data["event_class"] = this.eventClass;
		var url = "{% url 'instant-post-msg' %}";
		function error(err) {
			console.log(err);
		}
		function action(response) {	
			if (response.data.ok == 1) {
				status = '<i class="fa fa-check" style="color:green"></i>&nbsp;{% trans "Message sent" %}';
				app.statusMsg(status);
				app.msgToSend = "";
			} else {
				var err = response.data.err;
				var errmsg = '<i class="fa fa-close" style="color:red"></i>&nbsp;'+err;
				app.errMsg(errmsg, true);
			}
			
		}
		this.postForm(url, data, action, error);
	},
	statusMsg: function(msg) {
		app.show("msg_status");
		app.msgStatus = msg;
		app.hide("msg_status", 2500);
	},
	errMsg: function(msg) {
		app.show("msg_status");
		app.msgStatus = msg;
	},
	hide: function(el, delay) {
		elem = this.get(el);
		var action = function() { elem.style.display = "none" };
		if (delay !== undefined) {
			setTimeout(function() {
				 action()
			}, delay);
		} else {
			action()
		}
	},
	show: function(el) {
		elem = this.get(el);
		elem.style.display = "block"
	},
	activateChannel: function(channel) {
		{% get_channels as channels %}
		{% for ch in channels %}
			var el = document.getElementById('{{ ch }}');
			if (el.classList.contains("label-success")) {
				el.classList.remove("label-success");
				el.classList.add("label-default");
			}
		{% endfor %}
		var chan = document.getElementById(channel);
		chan.classList.remove("label-default");
		chan.classList.add("label-success");
		if (this.activeChannel === "") {
			// init
			document.getElementById("submitMsg").classList.remove("disabled");
			this.getEventClasses();
		}
		this.activeChannel = channel;
		var msg = "{% trans 'Publish message in channel' %} "+channel;
		this.instantFormPlaceholder = msg;
	},
	getEventClasses: function() {
		var event_classes = this.ecs();
		for (i=0;i<event_classes.length;i++) {
			this.eventLabels.push( {"name":event_classes[i], "label":get_label(event_classes[i])} );
		}
	},
	activateEventClass: function(cl) {
		this.eventClass = cl;
		var event_classes = this.ecs();
		for (i=0;i<event_classes.length;i++) {
			var ec = document.getElementById(event_classes[i]);
			ec.style.opacity = "0.6";
			}
		if (cl === this.eventClass) {
			var ec = document.getElementById(cl);
			ec.style.opacity = "1";
		}
	},
{% endif %}
toggleSidebar: function() {
	sidebar = this.get("sidebar");
	//console.log("CLASS", sidebar.className);
	if (this.sidebar) {
		//console.log("IS UP");
		this.sidebar = false;
		sidebar.className = "hidden";
	} else {
		//console.log("IS DOWN");
		this.sidebar = true;
		sidebar.className = "flex";
	}
	//console.log("CLASS", sidebar.className);
},
ecs: function() {
	return ['default', 'important', 'ok', 'info', 'debug', 'warning']
},
formatMsg: function(msg) {
	var event_classes = this.ecs();
	var label = "";
	for (i=0;i<event_classes.length;i++) {
		if (msg.event_class !== "default") {
			if (event_classes[i] === msg.event_class) {
				label = get_label(event_classes[i]);
				break
			}
		}
	}
	var res = label;
	res = res+"&nbsp;"+msg.message;
	return res
},
delMsg: function(msg) {	
	for (i=0;i<this.msgs.length;i++) {
		if (msg.uid === this.msgs[i].uid) {
			var index = this.msgs.indexOf(msg);
			this.msgs.splice(index, 1);
			this.numMsgs--;
			break
		}
	}
	if (this.numMsgs === 0) {
		if (this.sidebar === true) {
			this.toggleSidebar()
		}
	}
},
deleteAllMsgs: function() {
	this.msgs = [];
	this.numMsgs = 0;
	if (this.sidebar === true) {
		this.toggleSidebar();
	}
},