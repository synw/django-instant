# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


levels = (("public", "Public"),
          ("users", "Users"),
          ("staff", "Staff"),
          ("superuser", "Superuser")
          )


class Channel(models.Model):
    slug = models.CharField(max_length=120, verbose_name=_(u"Name"),
                            help_text=_(u"Use $ to prefix non public channels: "
                                        "ex: $private_chan"))
    role = models.CharField(max_length=20, choices=levels,
                            verbose_name=_(u"Authorized for"))
    handler = models.TextField(blank=True,
                               verbose_name=_(u"Javascript handler"))
    paths = models.CharField(max_length=255, blank=True, null=True,
                             verbose_name=_(u"Connect from paths"))
    active = models.BooleanField(default=True, verbose_name=_(u"Active"))

    class Meta:
        verbose_name = _(u'Channel')
        verbose_name_plural = _(u'Channels')

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        commit = False
        # chack channel name
        if self.role != "public":
            if self.slug.startswith("$") is False:
                self.slug = "$" + self.slug
                commit = True
        # check paths
        if self.paths == "":
            self.paths = None
            commit = True
        if commit is True:
            self.save()
        return super(Channel, self).save(*args, **kwargs)
