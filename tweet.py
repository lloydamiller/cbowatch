"""
 Takes a tweet, opens up the API connection and pushes the new tweet
"""

import tweepy
import apikeys as keys
import logging


def push_tweet(tweet_text):
    auth = tweepy.OAuthHandler(keys.API_KEY, keys.API_KEY_SECRET)
    auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    try:
        api.update_status(tweet_text)
        return 1
    except tweepy.TweepError as e:
        logging.error("Error posting tweet: %s" % e.message)
        return 0
