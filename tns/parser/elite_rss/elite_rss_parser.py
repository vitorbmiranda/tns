import feedparser
import logging.config
import re

from tns.parser.elite_rss.model.feeditem import FeedItem
from tns.parser.elite_rss.exception.elite_rss_exceptions \
    import EliteFeedParseInvalidHttpStatusException, EliteFeedParseNoLastIDException
import tns.db.service.meta_info as meta_info_service
import tns.cfg.config as config

logger = logging.getLogger(__name__)


def get_feed():
    """
    Parse the-elite's RSS feed and return a list of items with info about the Record.

    :return: list of feed items
    """

    # list of FeedItem
    feed_items = []

    logger.info("Starting the-elite's RSS feed parse")

    try:

        feed_uri = config.app_config['elite_rss_feed_uri']
        logger.debug("Using URI: " + feed_uri)

        feed_root = feedparser.parse(feed_uri)

        if not feed_root.status or feed_root.status != 200:
            raise EliteFeedParseInvalidHttpStatusException()

        logger.debug("Feed parsed successfully!")
        f_rss_pubdate = feed_root['feed']['published']

        logger.debug("Feed published date: {0}".format(f_rss_pubdate))

        all_items = feed_root['entries']

        # get the last ID stored in the meta_info table
        last_id = meta_info_service.get_last_id_meta_info().value

        if not last_id:
            raise EliteFeedParseNoLastIDException()

        # navigate through item list and create new FeedItem object
        for item in all_items:

            # get the data from the tuple
            f_title = item['title']
            f_link = item['link']
            f_description = item['description']
            f_pubdate = item['published']
            f_game = item['rnk_gameinitials']
            f_is_wr = item['rnk_worldrecord']
            f_is_untied_wr = item['rnk_untiedworldrecord']
            f_player_name = item['rnk_playername']
            f_player_alias = item['rnk_playeralias']
            f_stage = item['rnk_stage']
            f_difficulty = item['rnk_difficulty']
            f_timehms = item['rnk_timehms']
            f_video_type = item['rnk_videotype']
            f_video_id = item['rnk_videoid']

            record_id = re.search('.*time\/(\d+)', item.link).group(1)

            logger.debug("Record ID: {0}".format(record_id))

            if int(record_id) <= int(last_id):
                break;

            # create a new FeedItem instance and add it to the list
            this_item = FeedItem(f_title, f_link, f_description, f_pubdate, f_game, f_is_wr, f_is_untied_wr,
                                 f_player_name, f_player_alias, f_stage, f_difficulty, f_timehms, f_video_type,
                                 f_video_id)
            feed_items.append(this_item)
            logger.debug("appended: {0}".format(this_item))

        logger.info("Finished the-elite's RSS feed parse! Items fetched: {0}".format(len(feed_items)))

        return list(reversed(feed_items))

    except Exception:
        logger.exception("Error parsing the-elite' RSS feed!")
