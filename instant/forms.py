# -*- coding: utf-8 -*-

from django import forms
from instant.conf import ENABLE_USERS_CHANNEL, ENABLE_STAFF_CHANNEL, ENABLE_SUPERUSER_CHANNEL, PUBLIC_CHANNEL, USERS_CHANNELS, STAFF_CHANNELS, SUPERUSER_CHANNELS


choices = [((PUBLIC_CHANNEL, 'Public'))]
if ENABLE_USERS_CHANNEL is True:
    for channel in USERS_CHANNELS:
        choices.append((channel, channel))
if ENABLE_STAFF_CHANNEL is True:
    for channel in STAFF_CHANNELS:
        choices.append((channel, channel))
if ENABLE_SUPERUSER_CHANNEL is True:
    for channel in SUPERUSER_CHANNELS:
        choices.append((channel, channel))


class BroadcastForm(forms.Form):
    message = forms.CharField(max_length=300, label="Message", widget=forms.Textarea(
        attrs={'rows': '2'}), required=True)
    event_class = forms.CharField(
        max_length=60, label="Event class", required=False)
    default_channel = forms.CharField(
        max_length=60, label="Channels", required=False, widget=forms.RadioSelect(choices=choices))
    channel = forms.CharField(
        max_length=60, label="Other channel", required=False)
