from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from .init import ensure_channel_is_private


LEVELS = (
    ("public", "Public"),
    ("users", "Users"),
    ("groups", "Groups"),
    ("staff", "Staff"),
    ("superuser", "Superuser"),
)


class ChannelManager(models.Manager):
    def for_user(self, user):
        filter_from = ["public", "users"]
        if user.is_superuser:
            filter_from.append("superuser")
        if user.is_staff:
            filter_from.append("staff")
        chans = Channel.objects.filter(
            is_active=True, groups__in=user.groups.all()
        ) | Channel.objects.filter(level__in=filter_from, is_active=True)
        return chans


class Channel(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name=_("Name"),
        unique=True,
        help_text=_("Use $ to prefix non public channels: " "ex: $private_chan"),
    )
    level = models.CharField(
        max_length=20,
        choices=LEVELS,
        verbose_name=_("Authorized for"),
        default="superuser",
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))
    groups = models.ManyToManyField(Group, blank=True, verbose_name=_("Groups"))
    objects = ChannelManager()

    class Meta:  # type: ignore
        verbose_name = _("Channel")
        verbose_name_plural = _("Channels")

    def __str__(self) -> str:
        return str(self.name)

    def save(self, *args, **kwargs):
        # check the channel name
        if self.level != "public":
            self.name = ensure_channel_is_private(self.__str__())
        return super(Channel, self).save(*args, **kwargs)
