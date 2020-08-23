# B.M. ASHIK MAHMUD
# Fianl - NDM WISE MTD SALES

import pandas as pd
import pyodbc as db
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt
import numpy as np

## Create Database connection ---------

connection = db.connect(
    'DRIVER={SQL SERVER};'
     'SERVER=137.116.139.217;'
     # 'SERVER=10.168.2.241;'
    'DATABASE=ARCHIVESKF;'
     'UID=sa;PWD=erp@123'
    # 'UID=sa;PWD=erp'
    )
query = """
SELECT [NDM].[NDMNAME] AS NDM
,SUM([OESalesDetails].[EXTINVMISC]) AS SALES
FROM [OESalesDetails]
LEFT JOIN [NDM] ON [OESalesDetails].AUDTORG = [NDM].[BRANCH]
Where 
([TRANSDATE] BETWEEN 
'20200701'
--convert(varchar(8),DATEADD(mm, DATEDIFF(mm, 0, GETDATE()), 0),112) --- FIRST DAY OF CURRENT MONTH
AND 
'20200701'
--convert(varchar(8),DATEADD(D,-1,GETDATE()),112) --- YESTERDAY
)
GROUP BY [NDM].[NDMNAME]
ORDER BY [NDM].[NDMNAME]
"""
data = pd.read_sql_query(query, connection)
print(data)

def number_decorator(number):
    number = round(number, 1)
    number = format(number, ',')
    number = number + ' K'
    return number


def thousand_K_number_decorator(number):
    number = int(number / 1000)
    number = format(number, ',')
    number = number + 'K'
    return number

#lINE CHARTS
NDM = data['NDM']
sales = data['SALES']

fig, ax = plt.subplots()
# plt.ylim(0,140000)
line1 = ax.plot(NDM,sales, color='red',marker = 'o')
plt.xticks(rotation=45, ha='right')

for Sales_person,sales in zip(NDM,sales):
      plt.text(Sales_person, sales, thousand_K_number_decorator(sales), weight='bold')

ax.legend(labels=('Sales', 'Day'), loc='upper center', bbox_to_anchor=(0.5, -0.25),
          fancybox=True, shadow=True, ncol=5)  # legend placed at lower right


plt.xlabel("NDM",  color='black', fontsize=14, fontweight='bold')
plt.ylabel("MTD SALES", color='black', fontsize=14, fontweight='bold')
plt.title('NDM Wise MTD Sales', fontweight='bold', color='#3e0a75',  fontsize=18)
plt.tight_layout()
# plt.savefig('Final_NDM_WiseMTDSales.png')
plt.show()
