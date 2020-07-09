# B.M.ASHIK MAHMUD
# TRAINING PYTHON - AssignmentSending Email
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ------------ Group email ----------------------------------------
msgRoot = MIMEMultipart('related')
me = 'erp-bi.service@transcombd.com'
to = ['ashik.mahmud@transcombd.com', '']
cc = ['', '']
bcc = ['', '']

recipient = to + cc + bcc

subject = "Test report "

email_server_host = 'mail.transcombd.com'
port = 25

msgRoot['From'] = me

msgRoot['To'] = ', '.join(to)
msgRoot['Cc'] = ', '.join(cc)
msgRoot['Bcc'] = ', '.join(bcc)
msgRoot['Subject'] = subject

msg = MIMEMultipart()
msgRoot.attach(msg)
#
# msgText = MIMEText('This is the alternative plain text message.')
# msgAlternative.attach(msgText)

msgText = MIMEText("""
                       <img src="cid:img1_2"><br>
                        <br>
                       """, 'html')

msg.attach(msgText)

# --------- Set Credit image in mail   -----------------------
img = open('F:/PythonLearning/PythonTraining/Training/two_image.png', 'rb')
img1_2 = MIMEImage(img.read())
img.close()

img1_2.add_header('Content-ID', '<img1_2>')
msgRoot.attach(img1_2)

# # ----------- Finally send mail and close server connection ---
server = smtplib.SMTP(email_server_host, port)
server.ehlo()
server.sendmail(me, recipient, msgRoot.as_string())
server.close()
print('Mail Send')