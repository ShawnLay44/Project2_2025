import RPi.GPIO as GPIO

import time

import smtplib

from email.message import EmailMessage

from datetime import datetime



# GPIO 设定

sensor_pin = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(sensor_pin, GPIO.IN)



# email infomation

from_email_addr = "1612830974@qq.com"

from_email_pass = "kipqviqwrhzwcjbb"

to_email_addr = "1956286306@qq.com"



# the time for checking

target_times = ["8:00","12:00","16:00","20:00"]

triggered_today = set()  

def send_email(subject, body):

    msg = EmailMessage()

    msg.set_content(body)

    msg['From'] = from_email_addr

    msg['To'] = to_email_addr

    msg['Subject'] = subject

    try:

        server = smtplib.SMTP('smtp.qq.com', 587)

        server.starttls()

        server.login(from_email_addr, from_email_pass)

        server.send_message(msg)

        print(f"[{datetime.now().strftime('%H:%M:%S')}] email has been sent：{subject}")

    except Exception as e:

        print("fail to send the email：", e)

    finally:

        server.quit()

def get_moisture_status():

    if GPIO.input(sensor_pin):

        return "it is dry！please water it", True

    else:

        return "no need for watering。", False



print(" SoilSensorEmail detecting...")

try:

    while True:

        now = datetime.now()

        current_time_str = now.strftime("%H:%M")


      
        for target in target_times:

   	     if target not in triggered_today and current_time_str == target:

                message, _ = get_moisture_status()

                subject = "warning for watering"

                body = f"time：{current_time_str}\ncondition：{message}"

                send_email(subject, body)

                triggered_today.add(target)



        if now.strftime("%H:%M") == "00:00":

            triggered_today.clear()

        time.sleep(10)  # detect every 10 seconds

except KeyboardInterrupt:

    GPIO.cleanup()

    print("system out")



