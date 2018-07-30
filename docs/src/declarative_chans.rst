Declare channels
================

To declare new channels in settings.py use this format:

.. highlight:: python

::

   ["channel_name", ["/path/where/to/connect/it"]]
   
   
If the second element of the tuple is set the channels will be connected only for the 
listed path. If not set the channel will autoconnect on every path. Example:

.. highlight:: python

::

   INSTANT_SUPERUSER_CHANNELS=[
      ["$mysite_admin1", ["/a/path", "/another/path"]],
      ['$mysite_admin2']
   ]
   INSTANT_STAFF_CHANNELS=[
      ["$mysite_staff1", ["/a/path"]],
      ['$mysite_staff2'],
   ]
   INSTANT_USERS_CHANNELS=[
      ['$mysite_users1'],
   ]
   INSTANT_PUBLIC_CHANNELS=[
      ['mysite_public1'],
      ['mysite_public2'],
   ]
 
**Important**: every private channel name must start with a dollar sign 
  
Be sure to configure auth urls if you use private channels: urls.py:

.. highlight:: python

::

   from instant.views import instant_auth
   
   urlpatterns = [
   	# ...
   	url(r'^centrifuge/auth/$', instant_auth, name='instant-auth'),
   	]
