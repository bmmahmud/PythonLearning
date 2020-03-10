import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
from matplotlib.patches import Patch

# colors
colors = ['#ffd868', '#75daad']


# ------------------------------------------------------------------
def joker(number):
    number = number / 1000
    number = int(number)
    number = format(number, ',')
    number = number + 'K'
    return number
# ---------------------------------------------------------------------

# Establish Connection
connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp@123')

outstanding_df = pd.read_sql_query(""" select
            SUM(CASE WHEN TERMS='CASH' THEN OUT_NET END) AS TotalOutStandingOnCash,
            SUM(CASE WHEN TERMS not like '%CASH%' THEN OUT_NET END) AS TotalOutStandingOnCredit

            from  [ARCOUT].dbo.[CUST_OUT]
            where AUDTORG = 'RNGSKF' AND [INVDATE] <= convert(varchar(8),DATEADD(D,0,GETDATE()),112)
                                    """, connection)

cash = int(outstanding_df['TotalOutStandingOnCash']) # remove index
credit = int(outstanding_df['TotalOutStandingOnCredit'])

data = [cash, credit] # make data as a standard formate
total = cash + credit
# total = format((cash + credit), ',')
print(total)

legend_element = [Patch(facecolor='#ffd868', label='Cash'),
                  Patch(facecolor='#75daad', label='Credit')]
# -------------------new code--------------------------


ca = joker(cash)
cre = joker(credit)

DataLabel = [ca, cre] #
# -----------------------------------------------------
fig, ax = plt.subplots()
# # #Data have added under here
wedges, labels, xxx = ax.pie(data, colors=colors, labels=DataLabel, autopct='%.1f%%', startangle=90, pctdistance=.7)
plt.setp(xxx, fontsize=14, color='black', fontweight='bold')
plt.setp(labels, fontsize=14, fontweight='bold')
ax.text(0, -.1, total, ha='center', fontsize=14, fontweight='bold', backgroundcolor='#00daff')

# draw circle
centre_circle = plt.Circle((0, 0), 0.50, fc='white')

fig = plt.gcf() # why?

fig.gca().add_artist(centre_circle) # why?
# Equal aspect ratio ensures that pie is drawn as a circle
plt.title('1. Total Outstanding', fontsize=16, fontweight='bold', color='#3e0a75')

ax.axis('equal')#equal space around shapes
plt.legend(handles=legend_element, loc='lower left', fontsize=11)
plt.savefig('aa.png')

#plt.show()
print('1. Terms wise Outstanding Generated')
