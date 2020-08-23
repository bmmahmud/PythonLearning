import xlrd
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from email import encoders
from email.mime.base import MIMEBase


def table_data():
    xl = xlrd.open_workbook('F:/PythonLearning/PythonTraining/Training/top20.xlsx')
    sh = xl.sheet_by_name('Sheet1')

    th = ""
    td = ""
    # Select all columns header name and placed All name in serial
    for i in range(0, 1):
        # th = th + "<th class=\"unit\"> ID</th>"

        for j in range(0, sh.ncols):
            th = th + "<th class=\"unit\">" + str(sh.cell_value(i, j)) + "</th>\n"
        th = th + "</tr>\n"

    # Now placed all data
    for i in range(1, sh.nrows):
        td = td + "<tr>\n"
        td = td + "<td class=\"idcol\">" + str(i) + "</td>"

        for j in range(1, 2):
            td = td + "<td class=\"idcol\">" + str(sh.cell_value(i, j)) + "</td>\n"
        for j in range(2, 7):
            td = td + "<td class=\"unit\">" + str(sh.cell_value(i, j)) + "</td>\n"
        for j in range(7, sh.ncols):
            td = td + "<td class=\"idcol\">" + str(int(sh.cell_value(i, j))) + "</td>\n"
        td = td + "</tr>\n"
    html = th + td
    return html




# ------------ Group email ----------------------------------------
msgRoot = MIMEMultipart('related')
me = 'erp-bi.service@transcombd.com'
to = ['rejaul.islam@transcombd.com','']
cc = [' biswas@transcombd.com', 'yakub@transcombd.com','']
bcc = ['ashik.mahmud@transcombd.com', '']

recipient = to + cc + bcc

subject = "Python Final Project by B.M. ASHIK MAHMUD "

email_server_host = 'mail.transcombd.com'
port = 25

msgRoot['From'] = me

msgRoot['To'] = ', '.join(to)
msgRoot['Cc'] = ', '.join(cc)
msgRoot['Bcc'] = ', '.join(bcc)
msgRoot['Subject'] = subject

msg = MIMEMultipart()
msgRoot.attach(msg)

msgText = MIMEText(""" 

<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<style>
	table {
		border-collapse: collapse;
		border: 1px solid gray;
		padding: 5px;
	}

	td {
		padding-top: 5px;
		border-bottom: 1px solid #ddd;
		text-align: left;
		white-space: nowrap;
		border: 1px solid gray;
		#text-align: justify;
	}

	th.unit {
		padding: 2px;
		border: 1px solid gray;
		background-color: #dcf045;
		width: 22px;
		font-size: 16px;
		white-space: nowrap;
	}

	td.idcol {
		text-align: right;
		white-space: nowrap;
		text-justify: inter-word;
	}
	</style>
</head>

<body>
    <p> <b>Dear Royal,</b> </p>
    <p>Here, I have Completed and attached my  Final assignment. Please check. </p>
    <img src="cid:img1"><br>
    <img src="cid:img2"><br>
    <img src="cid:img3"><br>
    <img src="cid:img6"><br>
    <h3 style='text-align:left'> Top 20 Cash Drop Credit</h3>
	<table> """ + table_data() + """ </table>
	<p>Thanks and Regards,</p>
    <p><b>B.M.ASHIK MAHMUD </b></p>
    <p>Information System Automation (ISA)</p>
</body>

</html>

""", 'html')

msg.attach(msgText)

# # # Attached files
file_location = 'F:/PythonLearning/PythonTraining/Training/top20.xlsx'
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msgRoot.attach(part)

# --------- Set Credit image in mail   -----------------------
# images 1
img = open('F:/PythonLearning/PythonTraining/Training/final/fig1.png', 'rb')
img1 = MIMEImage(img.read())
img.close()

img1.add_header('Content-ID', '<img1>')
msgRoot.attach(img1)

# images 2
img =open('F:/PythonLearning/PythonTraining/Training/final/fig2.png', 'rb')
img2 = MIMEImage(img.read())
img.close()

img2.add_header('Content-ID', '<img2>')
msgRoot.attach(img2)

# images 3
img =open('F:/PythonLearning/PythonTraining/Training/final/fig3.png', 'rb')
img3 = MIMEImage(img.read())
img.close()

img3.add_header('Content-ID', '<img3>')
msgRoot.attach(img3)

# images 5
img =open('F:/PythonLearning/PythonTraining/Training/final/fig5.png', 'rb')
img6 = MIMEImage(img.read())
img.close()

img6.add_header('Content-ID', '<img6>')
msgRoot.attach(img6)

# # ----------- Finally send mail and close server connection ---
server = smtplib.SMTP(email_server_host, port)
server.ehlo()
server.sendmail(me, recipient, msgRoot.as_string())
server.close()
print('Mail Send')