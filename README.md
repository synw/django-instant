# Django Instant

Websockets for Django with [Centrifugo](https://github.com/centrifugal/centrifugo).

* Push events into public or private channels.

* Handle the events in javascript client-side.

* Works with an existing Django instance: it does not require any modification of your main stack.

Check the [documentation](http://django-instant.readthedocs.io/en/latest/).

### Quick example

Push some events on channels from anywhere in the code:

  ```python
from instant import broadcast
  
# push an event on the default public channel
broadcast(message='Message for everyone', event_class="test")

# push an event to the logged in users channel
broadcast(message='Message for users', target="users")

# push an event to the staff channel with an extra data payload
data = {"field1":"value1","field2":"value2"}
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

[Jafeed](https://github.com/synw/jafeed): rss feeds aggregator with live notifications on new posts

[Django Mqueue Livefeed](https://github.com/synw/django-mqueue-livefeed): real time application events and logs

[Django Presence](https://github.com/synw/django-presence): user presence notification widget

[Django Rechat](https://github.com/synw/django-rechat): basic chat app