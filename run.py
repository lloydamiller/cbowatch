# Core Python Script For Cycling Through

from datetime import datetime
import time
from rssfeed import get_new_feed_entries
from tweettext import make_tweet_text
from tweet import push_tweet

if __name__ == '__main__':

    last_run = False  # resets after first successful run.
    last_item = ''

    # initialize logger for Cycle module
    while True:
        current_time = datetime.now()

        if not last_run:
            run_condition = True

        else:
            # True if the program has not has a successful cycle during the current hour
            has_not_run_this_hour = last_run.hour != current_time.hour and last_run.day != current_time.day

            # True if it is every fourth hour (0, 4, 8, 12, 16, 20)
            every_fourth_hour = current_time.hour % 2 == 0

            run_condition = every_fourth_hour and has_not_run_this_hour

        if not run_condition:
            print("[*] Not Ready To Run")
            time.sleep(360)

        else:
            # open RSS feed check for new items
            print("[*] Opening RSS Feed")
            new_entries = get_new_feed_entries(last_item)

            print("[*] Found %i new entries" % len(new_entries))
            # for each new item, process for Tweet Text
            tweets = []
            print("[*] Generating tweet text")
            for new_entry in new_entries:
                tweet = make_tweet_text(new_entry['title'], new_entry['link'])
                tweets.append(tweet)
            # post new Tweet to Twitter

            new_tweets = 0
            if len(new_entries) > 0:
                print("[*] Publishing tweets")
                for tweet in tweets:
                    new_tweets += push_tweet(tweet)
                last_item = new_entries[0]['link']
                print("[*] Publishing %i new tweets" % new_tweets)
            else:
                print("[*] No new entries to update at this time.")
            last_run = datetime.now()
            time.sleep(60)

    pass
