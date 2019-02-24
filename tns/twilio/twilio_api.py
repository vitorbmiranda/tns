import logging.config
import tns.cfg.config as config

from twilio.rest import Client

logger = logging.getLogger(__name__)


def send_sms_message(to_number, body):

    twilio_config = config.app_config['twilio']
    is_live_mode = twilio_config['live_mode']

    if is_live_mode:
        twilio_credentials = twilio_config['credentials']['live']
    else:
        twilio_credentials = twilio_config['credentials']['test']

    account_sid = twilio_credentials['sid']
    auth_token = twilio_credentials['token']
    from_number = twilio_credentials['from']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=to_number,
        from_=from_number,
        body=body)
