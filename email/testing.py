import smtplib
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender = "cs50p2022@mail.com"
email_pass = "thisisCS50P!"
recipient = "muhammadbobat99@gmail.com"
subject = "Python"

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = subject

body = "Hi there, sending this attachment from python!"
msg.attach(MIMEText(body,'plain'))

filename = "passwords.txt"
attachment = open(filename, "rb")

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)


msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP("smtp.mail.com",587)
server.starttls()
server.login(sender, email_pass)


server.sendmail(sender, recipient, text)
server.quit()

