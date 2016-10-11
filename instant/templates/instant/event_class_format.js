function get_label(event_class) {
	var event_classes={
            'default' : 'mq-label mq-default',
            'important' : 'mq-label mq-important',
            'ok' : 'mq-label mq-ok',
            'info' : 'mq-label mq-info',
            'debug' : 'mq-label mq-debug',
            'warning' : 'mq-label mq-warning',
            'error' : 'mq-label mq-error',
            'object created' : 'mq-label mq-created',
            'object edited' : 'mq-label mq-edited',
            'object deleted' : 'mq-label mq-deleted',
            }
	var event_icons = {
            'default' : '<i class="fa fa-flash"></i>',
            'important' : '<i class="fa fa-exclamation"></i>',
            'ok' : '<i class="fa fa-thumbs-up"></i>',
            'info' : '<i class="fa fa-info-circle"></i>',
            'debug' : '<i class="fa fa-cog"></i>',
            'warning' : '<i class="fa fa-exclamation"></i>',
            'error' : '<i class="fa fa-exclamation-triangle"></i>',
            'object edited' : '<i class="fa fa-pencil"></i>',
            'object created' : '<i class="fa fa-plus"></i>',
            'object deleted' : '<i class="fa fa-remove"></i>',
            }
	var css_event_class = event_classes['default']
	for (ec in event_classes) {
		if ( event_class.toLowerCase() == ec.toLowerCase() ) {
			var ecl = event_class.toLowerCase()
			css_event_class = event_classes[ecl]
			icon_event_class = event_icons[ecl]
		}
	}
	var label = '<span class="'+css_event_class+'">'+icon_event_class+'&nbsp;&nbsp;'+event_class.toTitleCase()+'</span>';
	return label
}