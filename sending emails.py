from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template
import smtplib

from config import hidden_email, password


recipients_email = input("Enter recipient's email: ")
recipients_name = input("Enter recipient's name: ")
subject = input("Enter Subject of the mail: ")
body_of_the_message = input("Enter the message: ")


try:

    temp = Template(Path("template.html").read_text())
    message = MIMEMultipart()
    message["from"] = "Cure Link"
    message["to"] = recipients_email
    message["subject"] = subject
    body = temp.substitute(name=recipients_name,
                           message=body_of_the_message)
    message.attach(MIMEText(body, "html"))

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(hidden_email, password)
        smtp.send_message(message)
        print("Sent")
except Exception as e:
    print(e)
