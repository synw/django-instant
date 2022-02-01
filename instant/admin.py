from django.contrib import admin

from instant.models import Channel


@admin.register(Channel)  # type: ignore
class ChannelAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "is_active"]
