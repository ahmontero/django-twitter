# -*- encoding: utf-8 -*-

"""
This class has been adapted from Twython. Thanks to Erik Scheffers.
"""

import urllib
import urlparse
import inspect

import oauth2 as oauth

from settings import REQUEST_TOKEN_URL
from settings import ACCESS_TOKEN_URL
from settings import AUTHORIZE_URL
from settings import AUTHENTICATE_URL


# Detect if oauth2 supports the callback_url argument to request
OAUTH_LIB_SUPPORTS_CALLBACK = 'callback_url'\
    in inspect.getargspec(oauth.Client.request).args


class AuthError(AttributeError):
    """
        Raised when you try to access a protected resource and it fails due\
        to some issue with your authentication.
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class Twitter(object):
    def __init__(self, twitter_token=None, twitter_secret=None,
                 oauth_token=None, oauth_token_secret=None, headers=None,
                 callback_url=None):
        # Needed for hitting that there API.
        self.request_token_url = REQUEST_TOKEN_URL
        self.access_token_url = ACCESS_TOKEN_URL
        self.authorize_url = AUTHORIZE_URL
        self.authenticate_url = AUTHENTICATE_URL
        self.twitter_token = twitter_token
        self.twitter_secret = twitter_secret
        self.oauth_token = oauth_token
        self.oauth_secret = oauth_token_secret
        self.callback_url = callback_url

        # If there's headers, set them, otherwise be an embarassing parent for\
        # their own good.
        self.headers = headers
        if self.headers is None:
            self.headers = {'User-agent': 'Django-Twitter Library V1.0'}

        consumer = None
        token = None

        if self.twitter_token is not None and self.twitter_secret is not None:
            consumer = oauth.Consumer(self.twitter_token, self.twitter_secret)

        if self.oauth_token is not None and self.oauth_secret is not None:
            token = oauth.Token(oauth_token, oauth_token_secret)

        # Filter down through the possibilities here - if they have a token, \
        # if they're first stage, etc.
        if consumer is not None and token is not None:
            self.client = oauth.Client(consumer, token)
        elif consumer is not None:
            self.client = oauth.Client(consumer)

    def get_authentication_tokens(self):
        """
            get_auth_url(self)

            Returns an authorization URL for a user to hit.
        """
        callback_url = self.callback_url or 'oob'
        request_args = {}
        if OAUTH_LIB_SUPPORTS_CALLBACK:
            request_args['callback_url'] = callback_url

        resp, content = self.client.request(self.request_token_url,
            "GET", **request_args)

        if resp['status'] != '200':
            raise AuthError("Seems something couldn't be verified "\
                "withyour OAuth junk. Error: %s, Message: %s" \
                % (resp['status'], content))

        request_tokens = dict(urlparse.parse_qsl(content))
        oauth_callback_confirmed = request_tokens\
            .get('oauth_callback_confirmed') == 'true'

        if not OAUTH_LIB_SUPPORTS_CALLBACK and callback_url != 'oob'\
            and oauth_callback_confirmed:
            import warnings
            warnings.warn("oauth2 library doesn't support OAuth 1.0a"\
                " type callback, but remote requires it")
            oauth_callback_confirmed = False

        auth_url_params = {'oauth_token': request_tokens['oauth_token']}

        # Use old-style callback argument
        if callback_url != 'oob' and not oauth_callback_confirmed:
            auth_url_params['oauth_callback'] = callback_url

        request_tokens['auth_url'] = self.authenticate_url + '?'\
            + urllib.urlencode(auth_url_params)

        return request_tokens

    def get_authorized_tokens(self):
        """
            get_authorized_tokens

            Returns authorized tokens after they go through the auth_url phase.
        """
        resp, content = self.client.request(self.access_token_url, "GET")
        return dict(urlparse.parse_qsl(content))
