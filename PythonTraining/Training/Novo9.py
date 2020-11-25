import os
import smtplib
from _datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd
import xlrd
import pyodbc

dirpath = os.path.dirname(os.path.realpath(__file__))

msgRoot = MIMEMultipart('related')
me = 'erp-bi.service@transcombd.com'
to = ['', 'ashik.mahmud@transcombd.com']
cc = ['', '']
bcc = ['', '']

recipient = to + cc + bcc

date = datetime.today()
today = str(date.day) + '-' + str(date.strftime("%b")) + '-' + str(date.year) + ' ' + date.strftime("%I:%M %p")
today1 = str(date.day) + '-' + str(date.strftime("%b")) + '-' + str(date.year)

# # ------------ Group email --------------------
subject = "Brand Wise Sales Data " + today
email_server_host = 'mail.transcombd.com'
port = 25

msgRoot['From'] = me
msgRoot['To'] = ', '.join(to)
msgRoot['Cc'] = ', '.join(cc)
msgRoot['Bcc'] = ', '.join(bcc)
msgRoot['Subject'] = subject

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

msgText = MIMEText("""
             <h2> Dear Sir, </h2>
             <p> Please check the attached file <b>Item Wise Sales</b>.</p>
            <br>
            <h3> Thanks & Regards </h3>
            <h4> Md. Alhama Ekbal Kanon </h4>
            <h5> Jr. System Analyst </h5>

             """, 'html')

conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=10.168.2.241;'
                      'DATABASE=ARCHIVESKF;'
                      'UID=sa;'
                      'PWD=erp;')

data_df = pd.read_sql_query(
    """ DECLARE @DATEFROM_VAL AS CHAR(8)
DECLARE @DATETO_VAL AS CHAR(8)
DECLARE @Day as varchar (2)
set @day= (select Right(CONVERT(varchar(10), GETDATE(), 112),2))

IF @day = 1 begin
       SET @DATEFROM_VAL=(select  convert(varchar(10),DATEADD(mm, DATEDIFF(mm,0,getdate())-1, 0), 112))
       SET @DATETO_VAL=(select convert(varchar(10),DATEADD(day,-1,DATEADD(MM, DATEDIFF(MM,0,GETDATE()),0)),112))
       end
ELSE begin
       SET @DATEFROM_VAL=(SELECT  convert(varchar(10),DATEADD(mm, DATEDIFF(mm, 0, GETDATE()), 0),112))
       SET @DATETO_VAL=(SELECT CONVERT(VARCHAR(10), GETDATE(), 112) AS [YYYYMMDD] )
       end

SELECT dbo.OESalesDetails.ITEM, dbo.prinfoskf.[DESC] as Description, 
SUM(dbo.OESalesDetails.QTYSHIPPED) AS [Quantity], SUM(dbo.OESalesDetails.EXTINVMISC) AS [Sales], 

Sum(case when TRANSDATE = CONVERT(VARCHAR(10), DATEADD(DAY,-1, GETDATE()), 112) THEN dbo.OESalesDetails.QTYSHIPPED else 0 end) as [Quantity],
Sum(case when TRANSDATE = CONVERT(VARCHAR(10), DATEADD(DAY,-1, GETDATE()), 112) THEN dbo.OESalesDetails.EXTINVMISC else 0 end) as [Sales]

FROM  dbo.OESalesDetails LEFT OUTER JOIN
dbo.prinfoskf ON rtrim(dbo.OESalesDetails.ITEM) = rtrim(dbo.prinfoskf.ITEMNO)
WHERE (dbo.OESalesDetails.PRICELIST <> '00') 

AND  (dbo.OESalesDetails.TRANSDATE BETWEEN @DATEFROM_VAL AND @DATETO_VAL) 

GROUP BY dbo.OESalesDetails.ITEM, dbo.prinfoskf.[DESC]
""", conn)

writer = pd.ExcelWriter('item_wise_sales.xlsx', engine='xlsxwriter')
data_df.to_excel(writer, sheet_name='Sheet1', index=False, startrow=1)
workbook = writer.book

worksheet = writer.sheets['Sheet1']
worksheet.set_column('B:B', 30)

merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter'})

worksheet.merge_range('C1:D1', 'MTD', merge_format)
worksheet.merge_range('E1:F1', 'Yesterday', merge_format)
worksheet.set_column('C:D', 12)
worksheet.set_column('E:F', 12)
worksheet.merge_range('A1:A2', 'Item', merge_format)
worksheet.merge_range('B1:B2', 'Description', merge_format)
writer.save()

msgAlternative.attach(msgText)
# # Mail Body
# Attached top 10 leave
part = MIMEBase('application', "octet-stream")
file_location = dirpath + './1.8.xlsx'
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msgRoot.attach(part)

# #----------- Finally send mail and close server connection -----
server = smtplib.SMTP(email_server_host, port)
server.ehlo()
print('\n-----------------')
print('Sending Mail')
server.sendmail(me, recipient, msgRoot.as_string())
print('Mail Send')
print('-------------------')
server.close()
