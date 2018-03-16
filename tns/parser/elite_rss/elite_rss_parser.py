import feedparser
import logging.config

from tns.parser.elite_rss.model.feeditem import FeedItem
from tns.parser.elite_rss.exception.elite_rss_exceptions import EliteFeedParseInvalidHttpStatusException
import tns.cfg.config as config

logger = logging.getLogger(__name__)


def get_feed():
    """
    Parse the-elite's RSS feed and return a list of items with info about the Record

    ** PS: talking to Thingy about adding more relevant info that could be useful to us,
    such as points gained, player ID, level name etc.

    :return: list of feed items
    """

    # list of FeedItem
    feed_items = []

    logger.info("Starting the-elite's RSS feed parse")

    try:

        feed_uri = config.app_config['elite_rss_feed_uri']
        logger.debug("Using URI: " + feed_uri)

        feed_root = feedparser.parse(feed_uri)

        if feed_root.status != 200:
            raise EliteFeedParseInvalidHttpStatusException()

        logger.debug("Feed parsed successfully!")
        f_rss_pubdate = feed_root['feed']['published']

        logger.debug("Feed published date: {0}".format(f_rss_pubdate))

        all_items = feed_root['entries']

        # navigate through item list and create new FeedItem object
        for item in all_items:

            # get the data from the tuple
            f_title = item['title']
            f_link = item['link']
            f_description = item['description']
            f_pubdate = item['published']

            # TODO: check if a PR in the list is older than our last fetched PR
            # if so, we stop reading the feed

            # create a new FeedItem instance and add it to the list
            this_item = FeedItem(f_title, f_link, f_description, f_pubdate)
            feed_items.append(this_item)
            logger.debug("appended: {0}".format(this_item))

        logger.info("Finished the-elite's RSS feed parse! Items fetched: {0}".format(len(feed_items)))

        return feed_items

    except Exception:
        logger.exception("Error parsing the-elite' RSS feed!")
        raise
