"""
These functions:
1. Open up CBO web page
2. Pull the report summary
3. Condense summary to short version based on character length
4. Construct full Tweet
5. Return Tweet Text

"""

from bs4 import BeautifulSoup
from summarizer import summarize
import requests


def make_tweet_text(report_title, report_link):

    page = requests.get(report_link).text
    soup = BeautifulSoup(page, 'html.parser')
    for script in soup("script"):
        script.extract()
    report_summary_text = ' '.join(list(map(lambda p: p.text, soup.find_all('p'))))

    report_summary = summarize(report_title, report_summary_text, count=1)
    report_summary = ' '.join(report_summary)
    report_summary = report_summary.replace('\n', '')
    report_summary = report_summary.replace('\t', '')

    tweet_text = """%s: %s""" % (report_title, report_summary)

    if len(tweet_text) > 275:
        tweet_text = tweet_text[:270] + "..."

    tweet_with_link = tweet_text + '\n\n' + report_link

    return tweet_with_link
