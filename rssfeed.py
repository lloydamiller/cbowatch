"""
These functions:
1. Open RSS Feed stream
2. Cycle through items and break once encountering last_item URL
3. Return title and link for each new report in a list:

[{
    'title': 'Report Name',
    'URL': 'Report URL',
}]

"""

import feedparser


feed = 'https://www.cbo.gov/publications/all/rss.xml'


def get_new_feed_entries(last_item):

    d = feedparser.parse(feed)

    new_reports = []

    for entry in d.entries:
        if entry.link == last_item:
            break

        new_entry = {
            'title': entry.title,
            'link': entry.link
        }
        new_reports.append(new_entry)

    return new_reports
