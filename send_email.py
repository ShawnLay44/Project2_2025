import smtplib

from email.message import EmailMessage

from_email_addr ="1612830974@qq.com"

from_email_pass ="kipqviqwrhzwcjbb"

to_email_addr ="1956286306@qq.com"

# Create a message object

msg = EmailMessage()

# Set the email body

body ="Hello from Raspberry Pi"

msg.set_content(body)

msg['From'] = from_email_addr

msg['To'] = to_email_addr

msg['Subject'] = 'TEST EMAIL'

server = smtplib.SMTP('smtp.qq.com', 587)

server.starttls()

server.login(from_email_addr, from_email_pass)

server.send_message(msg)

print('email sent')

server.quit()
