'''
Created on Mar 20, 2012

@author: root
'''
import tweepy

def send(message):
    #Get some infor follow from Twitter App Creator
    #Consumer key
    consumer_key="consumer key"
    #Consumer secret
    consumer_secret="consumer secret"
    #Access token
    access_token="access token"
    #Access token secret
    access_token_secret="access token secret"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    #print api.me().name
    api.update_status(message)