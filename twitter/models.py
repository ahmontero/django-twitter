# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class ProfileUser(models.Model):
    user = models.OneToOneField(User)
    oauth_token = models.CharField(max_length=200,
        verbose_name=_("Oauth Token"))
    oauth_secret = models.CharField(max_length=200,
        verbose_name=_("Oauth Secret"))

    def __unicode__(self):
        return u"%s" % self.username
