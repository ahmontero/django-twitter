# -*- encoding: utf-8 -*-

from django.dispatch import Signal

# Tokens are received from Twitter
tokens_received = Signal(providing_args=['request', 'screen_name',
                                         'oauth_token', 'oauth_token_secret'])
