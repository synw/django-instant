# Django Instant

Websockets for Django with [Centrifugo](https://github.com/centrifugal/centrifugo).

* Push events into public or private channels.
* Handle the events in javascript client-side.

:sunny: Compatible: plug it on an existing Django instance _without any modification in your main stack_

### Example

Push events in channels from anywhere in the code:

  ```python
from instant.producers import publish
  
# Publish to a public channel
publish("public", "Message for everyone")

# Publish to a private channel with an event class set
publish("$users", "Message in logged in users channel", event_class="important")

# Publish to a group channel
publish("$group1", "Message for users in group1")

# Publish to the staff channel with an extra json data payload
data = {"field1":"value1","field2":[1,2]}
publish("$staff", "Message for staff", data=data)
  ```

## Quick start

### Install the Django package

```
pip install django-instant
```

Add `"instant"` to `INSTALLED_APPS` and update `urls.py`:

```python
urlpatterns = [
    # ...
    path("instant/", include("instant.urls")),
]
```

### Install the websockets server

#### Using the installer

Use the Centrifugo installer management command (for Linux and MacOs):

```
python manage.py installws
```

This will download a Centrifugo binary release and install it under a *centrifugo* directory. It will
generate the Django settings to use.

#### Install manualy

Install the Centrifugo websockets server (see the [detailled doc](https://centrifugal.github.io/centrifugo/server/install/) 
for more info). [Download a release](https://github.com/centrifugal/centrifugo/releases/latest) 
and generate a configuration file:

```
./centrifugo genconfig
```

The generated `config.json` file looks like this:

```javascript
{
  "v3_use_offset": true,
  "token_hmac_secret_key": "46b38493-147e-4e3f-86e0-dc5ec54f5133",
  "admin_password": "ad0dff75-3131-4a02-8d64-9279b4f1c57b",
  "admin_secret": "583bc4b7-0fa5-4c4a-8566-16d3ce4ad401",
  "api_key": "aaaf202f-b5f8-4b34-bf88-f6c03a1ecda6",
  "allowed_origins": []
}
```

### Configure the Django settings

Use the parameters from the installer's output or from Centrifugo's `config.json` file 
to update your Django's `settings.py`:

```python
CENTRIFUGO_HOST = "http://localhost"
CENTRIFUGO_PORT = 8001
CENTRIFUGO_HMAC_KEY = "46b38493-147e-4e3f-86e0-dc5ec54f5133"
CENTRIFUGO_API_KEY = "aaaf202f-b5f8-4b34-bf88-f6c03a1ecda6"
SITE_NAME = "My site" # used in the messages to identify where they come from
```

### Create channels

Go into the admin to create channels

## Avalailable endpoints

`/instant/login/`: takes a username and password as parameter and will login the
user in Django and return a Centrifugo connection token

`/instant/get_token/`: get a Centrifugo connection token for a logged in user

The two methods above return some connection information: a token for
the websockets connection, a Django csrf token and a list of authorized
channels for the user:

```javascript
{
  "csrf_token": "fvO61oyhcfzrW3SjPCYxYfzDAQFO6Yz7yaAQkxDbhC0NhlwoP1cecqLEYv8SCDLK",
  "ws_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJnZ2ciLCJleHAiOjE2M..",
  "channels": [
    {
      "name": "public",
      "level": "public"
    },
    {
      "name": "$users",
      "level": "users"
    },
    {
      "name": "$group1",
      "level": "groups"
    }
  ]
}
```

`/instant/subscribe/`: get tokens for Centrifugo channels subscriptions 
([doc](https://centrifugal.github.io/centrifugo/server/private_channels/))

## Publish method

The required parameters are `channel` and either `message` or `data`

```python
publish("$users", "A message", data={
        "foo": "bar"}, event_class="important", bucket="notifications")
```

The other parameters are optional

## Javascript client

A dedicated [javascript client](https://github.com/synw/djangoinstant) is available
to handle the messages and connections client side

## Example

An [example](https://github.com/synw/django-instant-example) with a backend and a frontend is available
