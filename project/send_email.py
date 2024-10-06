import os
from email.message import EmailMessage
import ssl
import smtplib


def email_sender(receiver, text):
    sender = "muhammadbobat99@gmail.com"
    email_pass = "nclurdapgiqcssjw"

    subject = "File of passwords"

    em = EmailMessage()
    em["From"] = sender
    em["To"] = receiver
    em["Subject"] = subject
    em.set_content(text)

    data = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=data) as smtp:
        smtp.login(sender, email_pass)
        smtp.sendmail(sender, receiver, em.as_string())