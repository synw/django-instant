Optionnal message labels
========================

Some javascript is used in the demo frontend to format the messages 
label: ``templates/instant/event_class_format.js``.

Some css classes are defined in ``instant/static/instant.css``. To customize:

.. highlight:: javascript

::
   
   {
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

Default icons (using font-awesome):

.. highlight:: javascript

::
   
   {
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
 