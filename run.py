# Core Python Script For Cycling Through

import tweepy
import apikeys as keys
from rssfeed import get_new_feed_entries
from tweettext import make_tweet_text


def push_tweet(tweet_text):
    auth = tweepy.OAuthHandler(keys.API_KEY, keys.API_KEY_SECRET)
    auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    try:
        api.update_status(tweet_text)
    except ConnectionError:
        print("OH NO, ERROR POSTING TWEET: %s" % tweet_text)

    return


if __name__ == '__main__':

    last_item = ''

    # open RSS feed check for new items
    new_entries = get_new_feed_entries(last_item)

    # for each new item, process for Tweet Text
    tweets = []
    for new_entry in new_entries:
        tweet = make_tweet_text(new_entry['title'], new_entry['link'])
        tweets.append(tweet)

    # post new Tweet to Twitter
    for tweet in tweets:
        # push_tweet(tweet)
        print(tweet)

    if len(new_entries) > 0:
        last_item = new_entries[0]['link']

    pass
