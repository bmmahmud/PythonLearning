# B.M. ASHIK MAHMUD
# Fianl - Branch Wise Live Sales

import pandas as pd
import pyodbc as db
from matplotlib import pyplot as plt
import numpy as np

## Create Database connection ---------

connection = db.connect(
    'DRIVER={SQL SERVER};'
    # 'SERVER=137.116.139.217;'
     'SERVER=10.168.2.241;'
    'DATABASE=ARCHIVESKF;'
    # 'UID=sa;PWD=erp@123'
    'UID=sa;PWD=erp'
    )
query = """
SELECT 
AUDTORG AS BRANCH
,Sum(EXTINVMISC) AS LIVE_SALES
FROM 
OESalesDetails
WHERE TRANSDATE = convert(varchar(8),DATEADD(D,0,GETDATE()),112)
GROUP BY AUDTORG
"""
data = pd.read_sql_query(query, connection)
print(data)

# -------------------Bar Charts---------------------------------
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


bar_index = np.arange(len(data['BRANCH']))
print(bar_index)

color = ['red', 'green', 'yellow', 'blue', 'orange', '#af5800']
# create plot
fig, ax = plt.subplots()

bar_width = .7
opacity = 0.9

bar1 = plt.bar(bar_index, data['LIVE_SALES'], bar_width,
               alpha=.6, color=color)

def autolabel(bar1):
    for bar in bar1:
        height = int(bar.get_height())
        ax.text(bar.get_x() - .3, 1 * height,
                thousand_K_number_decorator(height),
                va='bottom', rotation=0,
                fontsize=6, fontweight='bold', color='red')

autolabel(bar1)
# plt.bar(bar_index, data['LIVE_SALES'], align='center', alpha=.6, color=color) # total_bar = totall bar, sales Bar hight,
plt.xticks(bar_index, data['BRANCH'],rotation=90, ha='right')
plt.ylabel('Sales')
plt.title('Branch Wise Live Sales')
plt.tight_layout()
plt.show()