import smtplib, sys, urllib2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from PIL import Image
import io

GMAIL_USERNAME = '*******@gmail.com'
GMAIL_PASS = '*******'
RECEPIENT = '*******@tmomail.net'
SNAP_URL='http://127.0.0.1:8080/?action=snapshot'
MESSAGE = "Print complete! Here is your thingy:"
ROTATE_IMAGE = False

def send():
        email = MIMEMultipart()
        envelope = MIMEMultipart('alternative')
        msg_text = MIMEText(MESSAGE, 'plain')
        msg_html = MIMEText(MESSAGE, 'html')
        u = urllib2.urlopen(SNAP_URL)
        image = Image.open(u)
        fp = io.BytesIO()
        if ROTATE_IMAGE: 
            image.rotate(180).save(fp, Image.registered_extensions()['.jpg'])
        else:
            image.save(fp, Image.registered_extensions()['.jpg'])
        img = MIMEImage(fp.getvalue(), 'jpeg; name="print.jpg"')
        img.add_header('Content-Disposition', 'attachment; filename="print.jpg"$
        img.add_header('Content-ID', '<thingy>')
        img.add_header('X-Attachment-Id', 'thingy')
        email['From'] = GMAIL_USERNAME
        email['To'] = RECEPIENT
        envelope.attach(msg_text)
        envelope.attach(msg_html)
        email.attach(envelope)
        email.attach(img)
        server = smtplib.SMTP( "smtp.gmail.com", 587 )
        server.starttls()
        server.login(GMAIL_USERNAME, GMAIL_PASS)
        server.sendmail( GMAIL_USERNAME, RECEPIENT, email.as_string())
        
send()