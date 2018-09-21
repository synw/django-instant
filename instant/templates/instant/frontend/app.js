{% load vv_tags i18n %}
var vvDebug = {% isdebug %};
const app = new Vue({
	el: '#app',
	mixins: [vvMixin],
    data () {
		return { {% include "instant/frontend/vues/data.js" %} }
	},
	methods: {
		{% include "instant/frontend/vues/methods.js" %}
	},
	watch: {
		{% include "instant/frontend/vues/watchers.js" %}
	},
});