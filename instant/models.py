# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _


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
    handler = models.TextField(blank=True,
                               verbose_name=_(u"Javascript handler"))
    paths = models.CharField(max_length=255, blank=True, null=True,
                             verbose_name=_(u"Connect from paths"))
    active = models.BooleanField(default=True, verbose_name=_(u"Active"))
    groups = models.ManyToManyField(Group, blank=True,
                                    verbose_name=_(u"Groups"))

    class Meta:
        verbose_name = _(u'Channel')
        verbose_name_plural = _(u'Channels')

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        # chack channel name
        if self.role != "public":
            if self.slug.startswith("$") is False:
                self.slug = "$" + self.slug
        # check paths
        if self.paths == "":
            self.paths = None
        return super(Channel, self).save(*args, **kwargs)
