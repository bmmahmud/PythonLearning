import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import pyodbc as db
from email.mime.image import MIMEImage
from PIL import Image, ImageDraw, ImageFont
import Test_totallout
import trainingDay2


dirpath = os.path.dirname(os.path.realpath(__file__))# Make the path dinamic
# connection = db.connect('DRIVER={SQL Server};'
#                         'SERVER=10.168.2.241;'
#                         'DATABASE=ARCHIVESKF;'
#                         'UID=sa;PWD=erp')
# cursor = connection.cursor()
# print('DB connect success')
img1 = Image.open(dirpath + "/aa.png")
widthx, heightx = img1.size
img2 = Image.open(dirpath + "/bb.png")
imageSize = Image.new('RGB', (1283, 481))
imageSize.paste(img1, (1, 0))
imageSize.paste(img2, (widthx+2, 0))
imageSize.save(dirpath + "/abc.png")
# -----------------------------------------------------------------
# ------------ Email Section --------------------------------------
# -----------------------------------------------------------------
msgRoot = MIMEMultipart('related')
me = 'erp-bi.service@transcombd.com'
to = 'ashik.mahmud@transcombd.com'
recipient = to
# ------------ Group email --------------------
date = datetime.today()
today = str(date.day) + '/' + str(date.month) + '/' + str(date.year) + ' ' + date.strftime("%I:%M %p")
subject = "SK+F Formulation Reports - " + today
email_server_host = 'mail.transcombd.com'
port = 25
msgRoot['to'] = recipient
msgRoot['from'] = me
msgRoot['subject'] = subject
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)
msgText = MIMEText("""  Hello This is a test message
                      <img src="cid:abc" > <br>
                      """, 'html')
msgAlternative.attach(msgText)
# Add image 1
fp = open(dirpath + '/abc.png', 'rb')
abc = MIMEImage(fp.read())
fp.close()
abc.add_header('Content-ID', '<abc>')
msgRoot.attach(abc)
## For single user
msgRoot['to'] = recipient
msgRoot['from'] = me
msgRoot['subject'] = subject
server = smtplib.SMTP(email_server_host, port)
server.ehlo()
print('Sending Mail')
server.sendmail(me, recipient, msgRoot.as_string())
print('Mail Sent')
server.close()