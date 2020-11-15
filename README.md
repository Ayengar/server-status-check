# server-status-check script checks avaliability of the server and sends an sms if destination is unreachable.
in order to work it needs:

1)registration on twilio

2)installed modules: twilio, requests, twisted, dotenv

3).env file in the same dir as python file, with your information.

For example:

sms_receiver=+9999999999 # phone number on which sms will arrive

sms_sender=   # phone number, received on twilio

TWILIO_ACCOUNT_SID =   #your twilio account sid

TWILIO_AUTH_TOKEN =    #your twilio account token
