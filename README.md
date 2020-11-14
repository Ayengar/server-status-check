# server-status-check script checks avaliability of the server and sends an sms if destination is unreachable.
in order to work it needs:
1)registration on twilio
2)installed modules: twilio, requests, twisted
3).env file in the same dir as python file, with your information. For example: sms_receiver=+9999999999, etc.
