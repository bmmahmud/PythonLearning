# Training - July 2
# Pie Chart

import pandas as pd
import pyodbc as db
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def numberInThousands(number):
    number = int(number / 1000)
    number = format(number, ',')
    number = number + 'K'
    return number


def numberInComma(number):
    number = int(number)
    number = format(number, ',')
    return number


conn = db.connect('DRIVER={SQL Server};'
                  'SERVER=137.116.139.217;'
                  'DATABASE=ARCHIVESKF;'
                  'UID=sa;PWD=erp@123')

outstanding_df = pd.read_sql_query(""" select
                    SUM(CASE WHEN TERMS='CASH' THEN OUT_NET END) AS TotalOutStandingOnCash,
                    SUM(CASE WHEN TERMS not like '%CASH%' THEN OUT_NET END) AS TotalOutStandingOnCredit
                    from  [ARCOUT].dbo.[CUST_OUT]
                    where [INVDATE] <= convert(varchar(8),DATEADD(D,0,GETDATE()),112)
                     """, conn)

cash = int(outstanding_df['TotalOutStandingOnCash'])
credit = int(outstanding_df['TotalOutStandingOnCredit'])
data = [cash, credit]
print(data)

colors = ['#f9ff00', '#ff8600']
legend_element = [Patch(facecolor='#f9ff00', label='Cash'),
                  Patch(facecolor='#ff8600', label='Credit')]

data_label = [numberInThousands(cash), numberInThousands(credit)]
print(data_label)

fig1, ax = plt.subplots()
pack_all, label, percent_value = ax.pie(data, labels=data_label, colors=colors, autopct='%.1f%%', textprops={
    'color': "Black"}, startangle=90, pctdistance=.5)

plt.setp(percent_value, fontsize=14, color='blue', fontweight='bold')
plt.setp(label, fontsize=14, fontweight='bold')
plt.title('Total Outstanding', fontsize=16, fontweight='bold', color='#3e0a75')
ax.axis('equal')
plt.legend(handles=legend_element, loc='best', fontsize=11)
plt.tight_layout()
plt.show()
