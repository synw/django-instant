# -*- coding: utf-8 -*-

from django import forms
from instant.utils import _get_public_channel

choices = [
           ('public', 'Public'), 
           ('user', 'User'),
           ('staff', 'Staff'),
           ('admin', 'Admin')
           ]

class BroadcastForm(forms.Form):
    message = forms.CharField(
                              max_length=300, 
                              label="Message", 
                              widget=forms.Textarea(attrs={'rows':'2'}), 
                              required=True
                              )
    event_class = forms.CharField(
                                  max_length=60, 
                                  label="Event class", 
                                  required=True
                                  )
    channel = forms.CharField(
                                  max_length=60, 
                                  label="Channel", 
                                  required=True,
                                  initial = _get_public_channel()
                                  )
    """
    channel = forms.CharField(
                              max_length=60, 
                              label="Channel", 
                              required=True, 
                              widget=forms.RadioSelect(choices=choices)
                              )
    """

        



