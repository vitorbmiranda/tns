import logging.config
import re

import tns.db.database as database
import tns.parser.elite_rss.elite_rss_parser as elite_rss_parser
import tns.db.service.meta_info as meta_info_service

from tns.db.model.player import Player
from tns.msg.model.message import PRMessage
from tns.msg.messenger import Messenger

logger = logging.getLogger(__name__)


def notify_everyone():
    """
    This is the method that will be called by each job instance created by the scheduler.
    That is, this will be executed every X seconds.
    """

    logger.info("Notification job starting")
    session = None

    try:
        # start a DB session
        session = database.Session()

        # get the RSS items (oldest ones first)
        feed_items = elite_rss_parser.get_feed()

        # total number of wr messages sent
        wr_messages_sent = 0

        # if anything was fetched
        if len(feed_items) > 0:

            # load the players in the database
            players = session.query(Player)

            # for every item in the feed
            for item in feed_items:

                record_id = re.search('.*time\/(\d+)', item.link).group(1)

                logger.debug("Checking PR '{0}'".format(item.title))

                # use the player name or player alias accordingly
                player_name_or_alias = item.player_name if item.game == 'ge' else item.player_alias

                # is the time a world record (double checking because we are already checking the wrs feeds only)
                is_wr = item.is_wr

                if is_wr:

                    # for every player in our database
                    for player in players:

                        # check the players subscriptions
                        logger.debug("Player: {0}".format(player))

                        player_subscriptions = player.subscriptions

                        # check within the subscriptions if the player should be notified
                        for sub in player_subscriptions:
                            if sub.subscription_type.key == 'SUB_WRS':
                                should_player_be_notified = True;

                        if should_player_be_notified:
                            message = PRMessage(player_name_or_alias, item.game, item.stage,
                                                item.difficulty, item.time_hms, 100)

                            messenger = Messenger()
                            messenger.send_wr_sms(player, message)
                            wr_messages_sent += 1

                        # TODO add multithreading
                        # https://www.quantstart.com/articles/Parallelising-Python-with-Threading-and-Multiprocessing

            last_id = record_id
            meta_info_service.update_last_id_meta_info(session, last_id)

        logger.info("Notification finished! WRs messages sent: {0}".format(wr_messages_sent))

    except:
        session.rollback()
        raise

    finally:
        session.commit()
        session.close()
