# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Channel


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "is_active"]
