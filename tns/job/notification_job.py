import logging.config

import tns.db.database as database
import tns.msg.messenger as messenger
import tns.parser.elite_rss.elite_rss_parser as elite_rss_parser

from tns.db.model.player import Player
from tns.msg.model.message import PRMessage

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

        # check feed

        # TODO perhaps we pass a parameter to filter only >= last execution date/PR?
        # this parameter would be stored in our 'meta_data' table
        feed_items = elite_rss_parser.get_feed()

        # if anything was fetched (assuming that we only fetch new prs filtering by date)
        if len(feed_items) > 0:

            # load the players in the database
            players = session.query(Player)

            # for every item in the feed
            for item in feed_items:
                logger.debug("Checking PR '{0}'".format(item.title))

                # TODO here we already can check if it's a WR or >= X pts - those aren't related to the user profile
                # this flag will be True if this time is a WR/UWR
                is_wr = True

                # TODO here we need to get how much points this record gave (either by rss - Thingy, or by our ranks parser)
                # this flag will be True if this time has over X points (e.g 80, we have to configure that)
                is_high_points = True

                # TODO use variables so we know how many players were notified
                # maybe even store every single player + subtype that was sent
                wr_messages_sent = 0

                # for every player
                for player in players:

                    # check the players subscriptions
                    logger.debug("Player: {0}".format(player))

                    # TODO here we check which subscriptions the player has
                    # get the user subscriptions
                    # player_subscriptions = player.subscriptions
                    # for each one, check if it fits the condition
                    # if so, send ONE sms (not one for every sub)

                    # TODO we need to define an ordering, e.g: WR > bops > X pointers
                    # have to adapt this to send one message accordingly

                    # TODO get the data from the 'item' object, we don't have everything yet
                    message = PRMessage("Din Mor", "GE", "Dam", "Agent", "0:50", 100)

                    messenger.send_wr_sms(player, message)
                    wr_messages_sent += 1


                    # TODO add multithreading
                    # https://www.quantstart.com/articles/Parallelising-Python-with-Threading-and-Multiprocessing

        logger.info("Notification finished! \n"
                    "WRs messages sent: {0}".format(wr_messages_sent))

    except:
        session.rollback()
        raise

    finally:
        session.close()
