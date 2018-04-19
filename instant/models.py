# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from .init import _ensure_channel_is_private


levels = (("public", "Public"),
          ("users", "Users"),
          ("groups", "Groups"),
          ("staff", "Staff"),
          ("superuser", "Superuser")
          )


class Channel(models.Model):
    slug = models.CharField(max_length=120, verbose_name=_(u"Name"), unique=True,
                            help_text=_(u"Use $ to prefix non public channels: "
                                        "ex: $private_chan"))
    role = models.CharField(max_length=20, choices=levels,
                            verbose_name=_(u"Authorized for"))
    active = models.BooleanField(default=True, verbose_name=_(u"Active"))
    groups = models.ManyToManyField(Group, blank=True,
                                    verbose_name=_(u"Groups"))
    paths = models.CharField(max_length=255, blank=True,
                             verbose_name=_(u"Connect from paths"))
    handler_template = models.CharField(max_length=255, blank=True,
                                        verbose_name=_(u"Handler template url"))
    handler = models.TextField(blank=True,
                               verbose_name=_(u"Javascript handler"))
    deserializer_template = models.CharField(max_length=255, blank=True,
                                             verbose_name=_(u"Deserializer template url"))
    deserializer = models.TextField(blank=True,
                                    verbose_name=_(u"Javascript deserializer"))

    class Meta:
        verbose_name = _(u'Channel')
        verbose_name_plural = _(u'Channels')

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        # chack channel name
        print("SAVE", self.role, self.slug)
        if self.role != "public":
            if self.slug.startswith("$") is False:
                self.slug = _ensure_channel_is_private(self.slug)
        # check paths
        if self.paths == "":
            self.paths = None
        return super(Channel, self).save(*args, **kwargs)
