import RPi.GPIO as GPIO

import time

import smtplib

from email.message import EmailMessage

from datetime import datetime

sensor_pin = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(sensor_pin, GPIO.IN)

# email
from_email_addr = "1612830974@qq.com"

from_email_pass = "kipqviqwrhzwcjbb"  

to_email_addr = "1956286306@qq.com"



# time of detection
schedule_times = ["08:00", "12:00", "16:00", "20:00"]



# send email

def send_email(subject, body):

    msg=EmailMessage()

    msg.set_content(body)

    msg['From'] = from_email_addr

    msg['To'] = to_email_addr

    msg['Subject'] = subject



try:
    server = smtplib.SMTP('smtp.qq.com', 587)

    server.starttls()

    server.login(from_email_addr, from_email_pass)

    server.send_message(msg)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] email has been sent to ：{subject}")

except Exception as e:
	print("fail to send email：", e)

finally:

        server.quit()

def get_moisture_status():

    if GPIO.input(sensor_pin):  # no water 1

        return "need water！", True

    else:

        return "we don't need water", False

# main loop

print(" checking for the plants")



try:

    while True:

        current_time = datetime.now().strftime("%H:%M")

        if current_time in schedule_times:

            message, needs_water = get_moisture_status()

            email_subject = " warning to water plants"

            email_body = f"time：{current_time}\condition：{message}"

            send_email(email_subject, email_body)
	    
            time.sleep(61)  # wait for one minute
        else:
            time.sleep(10)

except KeyboardInterrupt:

    GPIO.cleanup()

    print(" system out")


