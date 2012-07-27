# -*- encoding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User
from django.views.generic import RedirectView

import signals

from toauth import Twitter


class RedirectToTwitterView(RedirectView):
    """
        This view initiates the handshake.
    """
    def get_redirect_url(self, *kwargs):
        current_url = self.request.META['HTTP_REFERER']
        self.request.session['django.twitter.current_url'] = current_url

        twitter = Twitter(twitter_token=settings.CONSUMER_KEY,
                          twitter_secret=settings.CONSUMER_SECRET)

        # Request an authorization url to send the user to
        auth_props = twitter.get_authentication_tokens()

        self.request.session['request_token'] = auth_props

        self.url = auth_props['auth_url']

        return super(RedirectToTwitterView, self).get_redirect_url(*kwargs)


class CallbackUrlView(RedirectView):
    """
        A user gets redirected here after hitting Twitter and authorizing your
        app to use their data.
        ***
            This view launchs the signal to your app with the tokens you want
        ***
    """
    permanent = True
    url = settings.CALLBACK_URL

    def get(self, request, *args, **kwargs):
        # Exchange magic tokens for permanent ones and raise signal
        twitter = Twitter(twitter_token=settings.CONSUMER_KEY,
                          twitter_secret=settings.CONSUMER_SECRET,
                          oauth_token=self.request\
                            .session['request_token']['oauth_token'],
                          oauth_token_secret=self.request\
                            .session['request_token']['oauth_token_secret'])

        authorized_tokens = twitter.get_authorized_tokens()
        screen_name = authorized_tokens['screen_name']
        oauth_token = authorized_tokens['oauth_token']
        oauth_token_secret = authorized_tokens['oauth_token_secret']

        signals.tokens_received.send(sender=User.__class__,
                                     request=request,
                                     screen_name=screen_name,
                                     oauth_token=oauth_token,
                                     oauth_token_secret=oauth_token_secret)

        current_url = request.session.get('django.twitter.current_url', False)
        if current_url:
            self.url = current_url
            del request.session['django.twitter.current_url']

        return super(CallbackUrlView, self).get(request, *args, **kwargs)
