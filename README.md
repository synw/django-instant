# Django Instant

Websockets for Django with [Centrifugo](https://github.com/centrifugal/centrifugo).

* Push events into public or private channels.

* Handle the events in javascript client-side.

:sunny: Just plug it on an existing Django instance: _it does not require any modification in your main stack_. 

Straightforward: no particular concepts to know, no learning curve: just push events and handle them client-side.

Check the [documentation](http://django-instant.readthedocs.io/en/latest/) for the install instructions.

### Quick example

Push events in channels from anywhere in the code:

  ```python
from instant.producers import broadcast
  
# push an event on the default public channel
broadcast(message='Message for everyone', event_class="test")

# push an event to the logged in users channel
broadcast(message='Message for users', target="users")

# push an event to the staff channel with an extra json data payload
data = {"field1":"value1","field2":[1,2]}
broadcast(message='Message for staff', target="staff", data=data)
  ```

Handle the events client-side in a template:

  ```javascript
if (event_class == 'test') {
        console.log("This is a test message: "+message);
        return true
}
  ```

### Example apps

[Django Mqueue Livefeed](https://github.com/synw/django-mqueue-livefeed): realtime application events and logs

[Django Presence](https://github.com/synw/django-presence): user presence notification widget

[Django Hitsfeed](https://github.com/synw/django-hitsfeed): realtime hits monitoring

[Jafeed](https://github.com/synw/jafeed): rss feeds aggregator with live notifications on new posts

[Django Rechat](https://github.com/synw/django-rechat): basic chat app

### Why?

Most of the websockets solutions associated with Django today require some modification in the main stack, like uwsgi, 
and often come with a whole bunch of new concepts to figure out, making the newcomer to feel like 
he is walking in the dark.

We wanted a solution that could plug on a safe classic Django stack without having to do any tweaks on it. 
The Centrifugo websockets server handles the job very well, better than all the python solutions I know IMHO. This made 
it possible to build an app that just plugs on an existing Django stack. The API is simple and does not involve any
new concept.

We are trying to ship a fully compatible, easy to install and ready to use websockets solution for Django: 
websockets in Django should not be a big deal!