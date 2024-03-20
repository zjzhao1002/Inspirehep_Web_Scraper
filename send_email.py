import smtplib
from email.mime.text import MIMEText

def send_email(body):
    subject = "You have new citations"
    sender = "<email address of the sender>"
    recipient = "<email address of the recipient>"
    password = "<sender password>"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients

    # codes are test by SMTP server of google
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(user=sender, password=password)
        smtp_server.sendmail(from_addr=sender, to_addrs=recipient, msg=msg.as_string())
    print("Message sent!")
