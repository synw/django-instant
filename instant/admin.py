# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Channel
from .forms import InstantAdminForm


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ["slug", "role"]
    form = InstantAdminForm
