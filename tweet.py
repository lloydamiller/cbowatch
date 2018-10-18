"""
 Takes a tweet, opens up the API connection and pushes the new tweet
"""

import tweepy
import apikeys as keys


def push_tweet(tweet_text):
    auth = tweepy.OAuthHandler(keys.API_KEY, keys.API_KEY_SECRET)
    auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    try:
        api.update_status(tweet_text)
    except tweepy.error.TweepError as e:
        print("[!] OH NO, ERROR POSTING TWEET: %s" % e.message)

    return
