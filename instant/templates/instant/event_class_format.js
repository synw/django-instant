function get_label(event_class) {
	var event_classes={
            'default' : 'mq-label mq-default',
            'important' : 'mq-label mq-important',
            'ok' : 'mq-label mq-ok',
            'info' : 'mq-label mq-info',
            'debug' : 'mq-label mq-debug',
            'warning' : 'mq-label mq-warning',
            'error' : 'mq-label mq-error',
            'created' : 'mq-label mq-created',
            'edited' : 'mq-label mq-edited',
            'deleted' : 'mq-label mq-deleted',
            }
	var event_icons = {
            'default' : '<i class="fa fa-flash"></i>',
            'important' : '<i class="fa fa-exclamation"></i>',
            'ok' : '<i class="fa fa-thumbs-up"></i>',
            'info' : '<i class="fa fa-info-circle"></i>',
            'debug' : '<i class="fa fa-cog"></i>',
            'warning' : '<i class="fa fa-exclamation"></i>',
            'error' : '<i class="fa fa-exclamation-triangle"></i>',
            'edited' : '<i class="fa fa-pencil"></i>',
            'created' : '<i class="fa fa-plus"></i>',
            'deleted' : '<i class="fa fa-remove"></i>',
            }
	var css_event_class = event_classes['default'];
	var icon_event_class = event_icons['default'];
	var event_class_lower = event_class.toLowerCase()
	var i = 0;
	for (event_type in event_classes) {
		if ( i > 0 ) {	
			if (event_class_lower.indexOf(event_type) !== -1) {
				css_event_class = event_classes[event_type];
				icon_event_class = event_icons[event_type];
				break
			}
		}
		i++;
	}
	var label = '<span class="'+css_event_class+'">'+icon_event_class+'&nbsp;&nbsp;'+event_class.toTitleCase()+'</span>';
	return label
}