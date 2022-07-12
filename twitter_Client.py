import os
import sys
from tweepy import API
from tweepy.auth import OAuthHandler

def get_twitter_auth():
    '''Setup Twitter Authentication
    
    
    return tweepy OAuthhandler object'''
    try:
        consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        access_token = os.environ['TWITTER_ACCESS_TOKEN']
        access_secret = os.environ['TWITTER_ACCESS_SECRET']
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)  #exits prog with an error
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth
    
def get_twitter_client():
    '''Setup Twitter Authentication
    
    
     return tweepy OAuthhandler object'''
    auth = get_twitter_auth()
    client = API(auth)
    return client
        
