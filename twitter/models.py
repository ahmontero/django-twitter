# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _


class OAuthProfile(models.Model):
    oauth_token = models.CharField(max_length=200,
        verbose_name=_("Oauth Token"))
    oauth_secret = models.CharField(max_length=200,
        verbose_name=_("Oauth Secret"))

    def __unicode__(self):
        return u"%s %s" % (self.oauth_token, self.oauth_secret)
