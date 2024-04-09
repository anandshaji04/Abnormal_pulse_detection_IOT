import conf, json, time
from boltiot import Email, Bolt
from boltiot import Sms, Bolt
minimum_limit = 57 #the minimum threshold of heart rate
maximum_limit = 100 #the maximum threshold of heart rate
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
mailer = Email(conf.MAILGUN_API_KEY, conf.SANDBOX_URL, conf.SENDER_EMAIL, conf.RECIPIENT_EMAIL)
sms = Sms(conf.SSID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
while True:
   response = mybolt.serialRead(2)
   data = json.loads(response)
   sensor_value = data['value']
   try:
       sensor_value = data['value']
       if sensor_value > maximum_limit or sensor_value < minimum_limit:
           response = mailer.send_email("Alert", "The Current Heart Rate is " +str(sensor_value))
           response = sms.send_sms("Alert! The Current Heart Rate is " +str(sensor_value))
   except Exception as e:
       print ()
   time.sleep(10)