import os
import smtplib
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from math import log, floor
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import pytz
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyodbc as db
import xlrd
from PIL import Image
from matplotlib.patches import Patch
import datetime as dd
import sys


def get_value(value):
    if (len(value) > 6):
        return str(value[0:len(value) - 6] + "," + value[len(value) - 6:len(value) - 3] + ","
                   + value[len(value) - 3:len(value)])
    elif len(value) > 3:
        return str(value[0:len(value) - 3] + "," + value[len(value) - 3:len(value)])
    elif (len(value) > 0):
        return value
    else:
        return "-"


dirpath = os.path.dirname(os.path.realpath(__file__))
connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp@123')
ClosedToMaturedcredit_df = pd.read_sql_query("""
               select CUSTOMER as 'Cust ID', CUSTNAME as 'Cust Name',
CustomerInformation.TEXTSTRE1 as 'Address', CustomerInformation.MSOTR as 'Territory',INVNUMBER as 'Inv Number',
convert(varchar,convert(datetime,(convert(varchar(8),INVDATE,112))),106)  as 'Inv Date', CustomerInformation.CREDIT_LIMIT_DAYS as 'Days Limit',
(datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)*-1 as 'Matured In Days', OUT_NET as 'Credit Amount'
from [ARCOUT].dbo.[CUST_OUT]
join ARCHIVESKF.dbo.CustomerInformation
on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
where  [ARCOUT].dbo.[CUST_OUT].AUDTORG = 'RNGSKF' and TERMS<>'Cash'
	and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)  between -3 and 0
	order by (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)desc
	, OUT_NET desc
 """, connection)
writer = pd.ExcelWriter('CashDropTable.xlsx', engine='xlsxwriter')
ClosedToMaturedcredit_df.index = np.arange(1, len(ClosedToMaturedcredit_df) + 1)
ClosedToMaturedcredit_df.to_excel(writer, sheet_name='Sheet1', index=True)
workbook = writer.book
worksheet = writer.sheets['Sheet1']
writer.save()


# ----------Table Data Create

def get_html_table2():
    xl = xlrd.open_workbook('CashDropTable.xlsx')
    sh = xl.sheet_by_name('Sheet1')
    th = ""
    td = ""
    for i in range(0, 1):
        th = th + "<tr>\n"
        th = th + "<th class=\"unit\">ID</th>"
        for j in range(1, sh.ncols):
            th = th + "<th class=\"unit\" >" + str(sh.cell_value(i, j)) + "</th>\n"
        th = th + "</tr>\n"
    for i in range(1, sh.nrows):
        td = td + "<tr>\n"
        td = td + "<td class=\"idcol\">" + str(i) + "</td>"
        for j in range(1, 2):
            td = td + "<td class=\"idcol\">" + str(sh.cell_value(i, j)) + "</td>\n"
        for j in range(2, 7):
            td = td + "<td class=\"unit\">" + str(sh.cell_value(i, j)) + "</td>\n"
        for j in range(7, sh.ncols):
            td = td + "<td class=\"idcol\">" + get_value(str(int(sh.cell_value(i, j)))) + "</td>\n"
        td = td + "</tr>\n"
    html = th + td
    return html


# -----Full page Design
all_table = """ <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <style>
                                    table
                                    {   
                                        width: 796px;
                                        border-collapse: collapse;
                                        border: 1px solid gray;
                                        padding: 5px;
                                    }
                                    td{
                                        padding-top: 5px;
                                        border-bottom: 1px solid #ddd;
                                        text-align: left;
                                        white-space: nowrap;
                                        border: 1px solid gray;
                                        text-align: justify;
                                        text-justify: inter-word;
                                    }
                                    th{
                                        padding: 2px;
                                        border: 1px solid gray;
                                        font-size: 10px !important;
                                        text-align:left;
                                        white-space: nowrap;
                                        text-align: justify;
                                        text-justify: inter-word;
                                    }
                                    th.table30tr{
                                        font-size:15px !important;
                                        height: 24px !important;
                                        background-color: brown;
                                        color: white;
                                        text-align: left;
                                        white-space: nowrap;
                                    }
                                    th.unit{
                                        background-color: #5ef28d;
                                        width:22px;
                                        font-size: 10px;
                                        white-space: nowrap;
                                        text-align: justify;
                                        text-justify: inter-word;
                                    }
                                    td.idcol{
                                        text-align: right;
                                        background-color: #efedf2;
                                        white-space: nowrap;
                                        font-size: 9px;
                                        text-justify: inter-word;
                                    }
                                    td.unit{
                                        background-color: #efedf2;
                                        white-space: nowrap;
                                        font-size: 9px;
                                        text-align: justify;
                                        text-justify: inter-word;
                                    }
                                    tr:hover {
                                        background-color:#f5f5f5;
                                    }
                                </style>
                            <title>Mail</title>
                        </head>
                        <body>
                        <table>
                            <p style="text-align:left"> """ + get_html_table2() + """</p>
                        </table>
                        </body>
                        </html>
                        """
# Mail part
msgRoot = MIMEMultipart('related')
me = 'erp-bi.service@transcombd.com'
to = 'ashik.mahmud@transcombd.com'
recipient = to
# ------------ Group email ---------------------------------------
# msgRoot = MIMEMultipart('related')
# me = 'erp-bi.service@transcombd.com'
# to = ['biswas@transcombd.com', 'yakub@transcombd.com']
# cc = ['zubair.transcom@gmail.com', 'aftab.uddin@transcombd.com']
# bcc = ['rejaul.islam@transcombd.com', 'fazle.rabby@transcombd.com']
#
# recipient = to+cc + bcc
date = datetime.today()
today = str(date.day) + '/' + str(date.month) + '/' + str(date.year) + ' ' + date.strftime("%I:%M %p")
today1 = str(date.day) + ' ' + str(date.strftime("%B")) + ' ' + str(date.year) + ' at ' + date.strftime("%I:%M %p")
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
# We reference the image in the IMG SRC attribute by the ID we give it below
html = """ 
        <div style="text-align:left" width='796px'> """ + all_table + """</div> 
         """
msgText = MIMEText("""
                     """ + all_table + """
                    """, 'html')
msgAlternative.attach(msgText)
# -------- Decleration group mail -----------------------------
# msgRoot['From'] = me
# msgRoot['To'] = ', '.join(to)
# msgRoot['Cc'] = ', '.join(cc)
# msgRoot['Bcc'] = ', '.join(bcc)
# msgRoot['Subject'] = subject
# ----------- Finally send mail and close server connection ---
server = smtplib.SMTP(email_server_host, port)
server.ehlo()
print('\n-----------------')
print('Sending Mail')
server.sendmail(me, recipient, msgRoot.as_string())
print('Mail Send')
print('-------------------')
server.close()
Html_file = open("Test.html", "w")
Html_file.write(html)
Html_file.close()

# Attached excel to Email
part = MIMEBase('application', "octet-stream")
file_location = dirpath + '/CashDropTable.xlsx'
# Create the attachment file (only do it once)
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msgRoot.attach(part)
