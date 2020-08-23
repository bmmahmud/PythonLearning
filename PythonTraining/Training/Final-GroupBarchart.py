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
salessql = """
        SELECT
        LEFT(TRANSDATE, 6) AS MONTHS
        ,SUM(EXTINVMISC) AS SALES
        FROM OESalesDetails
        where
        (TRANSDATE between
        convert(varchar(8),DATEADD(YEAR, DATEDIFF(YEAR, 0, GETDATE()), 0),112) ---First day of the YEAR
        AND
        convert(varchar(8),DATEADD(day,-1,DATEADD(MM, DATEDIFF(MM,0,GETDATE()),0)),112) -- Last day of last month
        )
        GROUP BY LEFT(TRANSDATE, 6)
        ORDER BY LEFT(TRANSDATE, 6)
"""
# ------------TARGET
targetsql = """
        select YEARMONTH AS MONTHS
        ,SUM([Target]) as TARGETS 
        from TDCL_BranchTarget
        where YEARMONTH between 
        convert(varchar(6),DATEADD(YEAR, DATEDIFF(YEAR, 0, GETDATE()), 0),112) --- FIRST MONTH
        AND
        convert(varchar(6),DATEADD(MONTH, DATEDIFF(MONTH, 0, GETDATE()) - 1, 0),112) --- PREVOUS MONTH
        group by YEARMONTH
"""

sales = pd.read_sql_query(salessql, connection)
target = pd.read_sql_query(targetsql, connection)
print(sales)
print(target)

def thousand_K_number_decorator(number):
    number = int(number / 1000)
    number = format(number, ',')
    number = number + 'K'
    return number

# ----------------------------
#
# # set width of bar
# barWidth = 0.25
#
# # set height of bar
# bars1 = sales['SALES']
# bars2 = target['TARGETS']
# bar_index = np.arange(len(target['MONTHS']))
# # Set position of bar on X axis
# r1 = np.arange(len(bars1))
# r2 = [x + barWidth for x in r1]
#
# # Make the plot
# plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='SALES')
# plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='TARGET')
#
# # Add xticks on the middle of the group bars
# plt.xlabel('MONTHS', fontweight='bold')
# # plt.xticks([r + barWidth for r in range(len(bars1))], ['A', 'B', 'C', 'D', 'E', 'F'])
# plt.xticks(bar_index, target['MONTHS'])
# # Create legend & Show graphic
# plt.legend()
# plt.show()

labels = sales['MONTHS']
men_means = sales['SALES']
women_means = target['TARGETS']

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='SALES')
rects2 = ax.bar(x + width/2, women_means, width, label='TARGET')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('TARGET VS SALES')
ax.set_title('MONTHLY TARGET VS SALES')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for bar in rects:
        height = int(bar.get_height())
        ax.text(bar.get_x() + .1, 1 * height,
                thousand_K_number_decorator(height),
                va='bottom', rotation=0,
                fontsize=8, fontweight='bold', color='red')


autolabel(rects1)
autolabel(rects2)

plt.tight_layout()

plt.show()