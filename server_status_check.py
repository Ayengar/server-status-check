import os
import logging
import requests
from twisted.internet import task, reactor
from twilio.rest import Client
from dotenv import load_dotenv

def check_availability():
    logging.info('Checking availability of server...')
    ping = requests.get('https://python101.online/')
    if ping.status_code != 200:
        logging.warning('SERVER IS DOWN!')

        load_dotenv()

        TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
        TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            body='Server is down!',  # текст сообщения
            sms_sender=os.getenv('sms_sender'),  # номер, который был получен
            sms_receiver=os.getenv('sms_receiver'),  # номер, на который придёт sms
            )
    else:
        logging.info('Server is available')

logging.basicConfig(filename='log_server_check',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
logger = logging.getLogger('log_server_check')

timeout = 60.0 #60 sec cooldown
work_executer = task.LoopingCall(check_availability)
work_executer.start(timeout)

reactor.run()
