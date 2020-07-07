# Assignment - 6
# B.M. ASHIK MAHMUD

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

#
# conn = db.connect('DRIVER={SQL Server};'
#                   'SERVER=137.116.139.217;'
#                   'DATABASE=ARCHIVESKF;'
#                   'UID=sa;PWD=erp@123')
#
# outstanding_df = pd.read_sql_query(""" select
#                     SUM(CASE WHEN TERMS='CASH' THEN OUT_NET END) AS TotalOutStandingOnCash,
#                     SUM(CASE WHEN TERMS not like '%CASH%' THEN OUT_NET END) AS TotalOutStandingOnCredit
#                     from  [ARCOUT].dbo.[CUST_OUT]
#                     where [INVDATE] <= convert(varchar(8),DATEADD(D,0,GETDATE()),112)
#                      """, conn)

# cash = int(outstanding_df['TotalOutStandingOnCash'])
# credit = int(outstanding_df['TotalOutStandingOnCredit'])
data = [700,300]
print(data)

# Center Circle Text
results = sum(data)
print(results)
total ='Total\n'+str(results)

# Define Color and lengend color
colors = ['#f08a5d', '#3ca59d']
legend_element = [Patch(facecolor='#f08a5d', label='A'),

                  Patch(facecolor='#3ca59d', label='E')]
# -------------------------

data_label = [700,300]
print(data_label)


fig1, ax = plt.subplots()
pack_all, label, percent_value = ax.pie(data, labels=data_label, colors=colors, autopct='%.1f%%', textprops={
    'color': "Black"}, startangle=90, pctdistance=.8)
ax.text(0,-.1,total,ha='center', fontsize=18, color='#d92027', fontweight='bold')
plt.setp(percent_value, fontsize=12, color='#120136', fontweight='bold')
plt.setp(label, fontsize=16, color='#035aa6',fontweight='bold')

# Center Circle and
centre_circle = plt.Circle((0,0),0.50,fc='white')
fig1.gca().add_artist(centre_circle)


plt.title('chart- D', fontsize=16, fontweight='bold', color='#303960')
ax.axis('equal')
plt.legend(handles=legend_element, loc='lower left', fontsize=11)
plt.tight_layout()
plt.savefig('figure-D.png')
plt.show()
