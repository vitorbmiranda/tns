from twilio.rest import Client

##
# To actually send a SMS message we have to use our "Live" credentials.
# The "Test" credentials are just to simulate a call to Twilio's API,
#  HOWEVER the from number has to be +15005550006 for a "successful" call.
# We can validate a few cases with other 'to' numbers aswell.

# https://www.twilio.com/docs/guides/testing-sms
# All the numbers: https://www.twilio.com/docs/api/rest/test-credentials#test-sms-messages
##

# get account SID and Auth Token from twilio.com/console
account_sid = ""
auth_token = ""

# to actually send an sms we have to get the number from twilio.com/console/phone-numbers/incoming
from_number = ""

# to number
to_number = ""

# message body
body = "Test!"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=to_number,
    from_=from_number,
    body=body)

print(message.sid)