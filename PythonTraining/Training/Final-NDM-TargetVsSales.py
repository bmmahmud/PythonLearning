# B.M. ASHIK MAHMUD
# NDM TARGET VS SALES

import pandas as pd
import pyodbc as db
from matplotlib import pyplot as plt
import numpy as np

## Create Database connection ---------

connection = db.connect(
    'DRIVER={SQL SERVER};'
     'SERVER=137.116.139.217;'
    #  'SERVER=10.168.2.241;'
    'DATABASE=ARCHIVESKF;'
    'UID=sa;PWD=erp@123'
    # 'UID=sa;PWD=erp'
    )
query = """
        SELECT [NDM].[NDMNAME]  AS NDM
        ,SUM([OESalesDetails].[EXTINVMISC]) AS SALES
        FROM [OESalesDetails]
        LEFT JOIN [NDM] ON [OESalesDetails].AUDTORG = [NDM].[BRANCH]
        Where 
        ([TRANSDATE] BETWEEN 
        --'20200701'
        convert(varchar(8),DATEADD(mm, DATEDIFF(mm, 0, GETDATE()), 0),112) --- FIRST DAY OF CURRENT MONTH
        AND 
        --'20200708'
        convert(varchar(8),DATEADD(D,-1,GETDATE()),112) --- YESTERDAY
        )
        GROUP BY [NDM].[NDMNAME]
        ORDER BY [NDM].[NDMNAME]
"""
# ------------TARGET
queryx = """
        SELECT [NDM].[NDMNAME] AS NDM
        ,SUM([TDCL_BranchTarget].[TARGET]) AS NDM_TARGET
        FROM [NDM]
        LEFT JOIN [TDCL_BranchTarget] ON 
        [NDM].[BRANCH]= [TDCL_BranchTarget].[AUDTORG]
        WHERE YEARMONTH =(convert(varchar(6),DATEADD(D,-1,GETDATE()),112))
        GROUP BY [NDM].[NDMNAME]
        ORDER BY [NDM].[NDMNAME]
"""

data = pd.read_sql_query(query, connection)
qqy = pd.read_sql_query(queryx, connection)
print(data)
print(qqy)


#
# # -------------------Bar Charts---------------------------------
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


# --------------------------------
bar_index = np.arange(len(data['NDM']))

# create plot
fig, ax = plt.subplots()

bar_width = 0.5
opacity = 0.9

bar1 = plt.bar(bar_index, data['SALES'], bar_width,
               alpha=opacity, color='#F1C40F')


plt.plot(qqy['NDM'], qqy['NDM_TARGET'],color='red',marker = 'o')
for Sales_person,Day1 in zip(qqy['NDM'], qqy['NDM_TARGET']):
       plt.text(Sales_person, Day1, str(int(Day1/1000))+'k', weight='bold')

def autolabel(bar1):
    for bar in bar1:
        height = int(bar.get_height())
        ax.text(bar.get_x() + .1, 1 * height,
                thousand_K_number_decorator(height),
                va='bottom', rotation=0,
                fontsize=8, fontweight='bold', color='red')


autolabel(bar1)

plt.ylabel('TARGET AND SALES', fontweight="bold")
plt.xlabel('NDM', fontweight="bold")
plt.title('NDM WISE MTD SALES', fontweight="bold")
plt.xticks(bar_index, qqy['NDM'])

ax.legend(labels=(['TARGET AND SALES', 'NDM']), loc='upper center', bbox_to_anchor=(0.5, -0.25),
          fancybox=True, shadow=True, ncol=5)  # legend placed at lower right

plt.tight_layout()
plt.show()
