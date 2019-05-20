# Core Python Script For Cycling Through

from datetime import datetime
import time
from rssfeed import get_new_feed_entries
from tweettext import make_tweet_text
from tweet import push_tweet
import logging


def main():
    last_cycle = False
    last_item = ""
    while True:
        if last_cycle is False:
            last_cycle = datetime.now()
        else:
            if last_cycle.hour == datetime.now().hour:
                time.sleep(3600)
                continue
            else:
                last_cycle = datetime.now()

        new_entries = get_new_feed_entries(last_item)

        tweets = []
        for new_entry in new_entries:
            tweet = make_tweet_text(new_entry['title'], new_entry['link'])
            tweets.append(tweet)

        # post new Tweet to Twitter
        new_tweets = 0
        if len(new_entries) > 0:
            for tweet in tweets:
                new_tweets += push_tweet(tweet)
            last_item = new_entries[0]['link']
            logging.info("Published %i new tweets" % new_tweets)
        else:
            logging.info("No new entries")
        time.sleep(60)


if __name__ == '__main__':
    logging_level = logging.INFO
    logging.basicConfig(handlers=[
                            logging.StreamHandler()
                        ], level=logging_level,
                        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.info("CBOWatch Bot Initiated")
    main()
