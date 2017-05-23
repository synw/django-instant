{% load i18n %}
{% if user.is_superuser %}
	instantForm: false,
	activeChannel: "",
	instantFormPlaceholder: "{% trans 'Select a channel' %}",
	msgToSend:"",
{% endif %}
eventClass: "default",
eventLabels: new Array,
msgs: [],
numMsgs: 0,
msgStatus: "",
msgIconClass: {
	"fa": true,
	"fa-envelope-o": true,
	"fa-envelope": false
},
autoMsg: false,
warningMsg: "",
infoMsg: "",
messages: "",
sidebar: false,