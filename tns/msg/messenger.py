import logging.config
import tns.msg.msg_formatter as msg_formatter
import tns.twilio.twilio_api as twilio_api
import tns.crypto.tns_crypto as tns_crypto

from tns.msg.utils import MessengerUtils

logger = logging.getLogger(__name__)


class Messenger:

    def __init__(self):
        self.utils = MessengerUtils()

    def send_wr_sms(self, to_player, message):
        """
        :param to_player: Player that will receive the message
        :param message: PRMessage object containing all the relevant info
        :return:
        """

        player_alias = to_player.alias
        logger.debug("Sending WR message to: {0}".format(player_alias))
        self.__send_sms(to_player, msg_formatter.wr_message(message))
        logger.debug("WR message sent succesfully to: {0}".format(player_alias))

    def __send_sms(self, to_player, final_message):
        """
        Calls the Twilio API to send the message

        :param to_player: Player that will receive the message
        :param final_message: final formatted message String
        """
        # TODO call the 'twilio' module to actually pass the message that will be sent

        # NEVER write the player's # in the log
        phone_number = to_player.phone_number

        logger.debug("Player's # number: {0}".format(self.utils.mask_phone_number(tns_crypto.decrypt(phone_number))))

        # twilio_api.send_sms_message(phone_number, final_message)