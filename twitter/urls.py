# -*- encoding: utf-8 -*-
from django.conf.urls.defaults import *

from views import CallbackUrlView, RedirectToTwitterView

urlpatterns = patterns('',
    url(r'^login/?$', RedirectToTwitterView.as_view(),
        name="twitter_begin_auth"),

    url(r'^callback/?$', CallbackUrlView.as_view(),
        name='twitter_callback_url'),
)
