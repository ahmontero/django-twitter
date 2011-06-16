django-twitter
==============
django-twitter is a django application that allows you to login into Twitter in a 
easy and unobstrusive way:\n

Write {{url twitte_bebin_auth}} in your view inside your template. /n
When the user is redirected from Twitter to your application, django-twitter raises token_received signal. /n
You can do whatever you want with the tokens received from Twitter. /n

How To Use
==========
1. Add 'twitter' to your apps list

2. Add in settings.py:
    CONSUMER_KEY = "your_consumer_key" /n
    CONSUMER_SECRET = "your_consumer_secret" /n
    AUTH_PROFILE_MODULE = 'twitter.ProfileUser' /n
    CALLBACK_URL = 'your_awesome_url' /n

CONSUMER_KEY: You can obtain it from your Twitter account. /n
CONSUMER_SECRET: You can obtain it from your Twitter account. /n
AUTH_PROFILE_MODULE: django-twitter uses an user profile to store the credentials from Twitter. /n
AUTH_PROFILE_MODULE: You need to specify this profile:'twitter.ProfileUser'./n
CALLBACK_URL: is the url inside your application that should be shown when the authentication process went ok. It must be same as Twitter callback url. /n

3. Connect with tokens_received signal: /n

from twitter import signals

def tokens_received(sender, request, screen_name, oauth_token, oauth_token_secret, **kwargs):
    #Your stuff here

signals.tokens_received.connect(tokens_received)

How it works
============
To insert the link to Twitter, in your template include this: '{% url twitter_begin_auth %}'. 
Then the user is redirected to Twitter. 
When the username and password is inserted, then redirects to CALLBACK_URL in your application and tokens_received signal is raised.

NOTE:
-----
Remember that your Twitter callback url must be the same as CALLBACK_URL

Dependencies
============
djano-twitter uses Django 1.3 and oauth2

References
==========
Some parts of Twython have been adapted to make possible this application. Thanks to Twython creator
for share with us so amazing code.
