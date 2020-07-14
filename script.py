import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from dotenv import load_dotenv


load_dotenv()

client = Client()


class TwillioMessanger:
    """call this class with the send() method to send a message 
	   returns true if message was sent successfully"""

    @classmethod
    def send(self, message, user_no):
        from_no = os.environ.get("FROM")
        to = f"whatsapp:{user_no}"
        try:
            sent = client.messages.create(body=message, from_=from_no, to=to)
            if sent:
                return True
        except TwilioRestException as err:
            return err
