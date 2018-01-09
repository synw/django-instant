{% load instant_tags i18n %}
const app = new Vue({
	el: '#app',
	mixins: [vvMixin],
    data () {
        return {
        	numMsgs: 0,
        	instantForm: false,
        	eventLabels: new Array,
        	instantFormPlaceholder: "{% trans 'Select a channel' %}",
        	msgToSend:"",
        	msgs: [],
        	errMsg: "",
        	msgStatus: "",
        	msgIconClass: {
        		"fa": true,
        		"fa-envelope-o": true,
        		"fa-envelope": false
        	},
        	activeChannel: "",
        }
	},
	methods: {
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
				app.setErrMsg(errmsg, true);
			}
			function action(response) {	
				if (response.data.ok == 1) {
					status = '<i class="fa fa-check" style="color:green"></i>&nbsp;{% trans "Message sent" %}';
					app.statusMsg(status);
					app.msgToSend = "";
				} else {
					var err = response.data.err;
					var errmsg = '<i class="fa fa-close" style="color:red"></i>&nbsp;'+err;
					app.setErrMsg(errmsg, true);
				}
				
			}
			this.postForm(url, data, action, error);
		},
		statusMsg: function(msg) {
			app.show("msg_status");
			app.msgStatus = msg;
			app.hide("msg_status", 2500);
		},
		setErrMsg: function(msg) {
			app.show("msg_status");
			app.msgStatus = msg;
		},
		activateChannel: function(channel) {
			{% get_all_channels as channels %}
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
		show: function(el) {
			elem = this.get(el);
			elem.style.display = "block"
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
	},
});
{% include "instant/event_class_format.js" %}
function typeOf (obj) {
  return {}.toString.call(obj).split(' ')[1].slice(0, -1).toLowerCase();
}
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = cookies[i].trim();
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
{% for appname, parts in apps.items %}
	{% include parts.extra %}
{% endfor %}
