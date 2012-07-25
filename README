django-twitter allows your users to login into your application using Twitter in a easy way.

How To Use
==========
1. Add 'twitter' to your apps list

2. Include('twitter.urls') in your url app

3. Add in settings.py:
    CONSUMER_KEY = "your_consumer_key"
    CONSUMER_SECRET = "your_consumer_secret"
    CALLBACK_URL = 'your_awesome_url'

CONSUMER_KEY: You can obtain it from your Twitter account.
CONSUMER_SECRET: You can obtain it from your Twitter account.
CALLBACK_URL: is the url inside your application that should be shown when the authentication process went ok. It must be same as Twitter callback url.

4. Connect with tokens_received signal:

from twitter import signals

def tokens_received(sender, request, screen_name, oauth_token, oauth_token_secret, **kwargs):
    #Your stuff here

signals.tokens_received.connect(tokens_received)

How it works
============
To insert the link to Twitter, include this in your template : {% url twitter_begin_auth %} in a link.
When the user click on the link, is redirected to Twitter, and once logged in, it will redirect you to CALLBACK_URL in your application and tokens_received signal will be raised.

NOTE:
-----
Remember that your Twitter callback url must be the same as CALLBACK_URL

Dependencies
============
djano-twitter uses Django 1.3 and oauth2

References
==========
Some parts of Twython have been adapted to make possible this application. Thanks to Twython creator for share with us so amazing code.
