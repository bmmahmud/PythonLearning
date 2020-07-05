# B.M. ASHIK MAHMUD
# Assignment 5

import pandas as pd
import pyodbc as db
from matplotlib import pyplot as plt
import numpy as np

## Create Database connection ---------

connection = db.connect(
    'DRIVER={SQL SERVER};'
    'SERVER=137.116.139.217;'
    'DATABASE=ARCHIVESKF;'
    'UID=sa;PWD=erp@123')
query = """
            DECLARE @Thisday CHAR(8) = CONVERT(varchar(8), dateAdd(day,-1,getdate()), 112)
            DECLARE @lastday CHAR(8) = CONVERT(varchar(8), dateAdd(DAY,-2,getdate()), 112)
            DECLARE @thismonth CHAR(6) = CONVERT(varchar(6), dateAdd(MONTH,0,getdate()-30), 112)
            select top 10 RSMTR as RSMTR, 
            SUM(case when TRANSDATE = @Thisday then EXTINVMISC END)  as YesterdaySales,
            SUM(case when TRANSDATE = @lastday then EXTINVMISC END) as BeforeTwodaysSales,
            SUM(case when transtype=2 and left(transdate,6) = @thismonth then EXTINVMISC*(-1) END) as ReturnVal
            from OESalesDetails
            group by RSMTR
            order by  YesterdaySales desc,   BeforeTwodaysSales desc, ReturnVal DESC
"""
data = pd.read_sql_query(query, connection)
# print(data)


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


# day1_sale = [9000, 5500, 4000, 6500]
# day2_sale = [8500, 6200, 5400, 2000]
# sales_person = ['Kuddus', 'Rubel', 'Rony', 'Rocky']
bar_index = np.arange(len(data['YesterdaySales']))

# create plot
fig, ax = plt.subplots()

bar_width = 0.5
opacity = 0.9

bar1 = plt.bar(bar_index, data['YesterdaySales'], bar_width,
               alpha=opacity, color='#F1C40F')
# fig, ax = plt.subplots()
# ax.plot( data['RSMTR'], data['ReturnVal'], color='red',marker = 'o')
plt.plot(data['RSMTR'], data['ReturnVal'],color='red',marker = 'o')
for Sales_person,Day1 in zip(data['RSMTR'], data['ReturnVal']):
      plt.text(Sales_person, Day1, str(int(Day1/1000))+'k', weight='bold')
# bar2 = plt.bar(bar_index + bar_width, day2_sale, bar_width,
#                alpha=opacity, color='r')


def autolabel(bar1):
    for bar in bar1:
        height = int(bar.get_height())
        ax.text(bar.get_x() + .1, 1 * height,
                thousand_K_number_decorator(height),
                va='bottom', rotation=0,
                fontsize=8, fontweight='bold', color='red')


# def autolabel(bar2):
#     for bar in bar2:
#         height = int(bar.get_height())
#         ax.text(bar.get_x() + .1, 0.8 * height,
#                 number_decorator(height),
#                 va='bottom', rotation=90,
#                 fontsize=12, fontweight='bold')


autolabel(bar1)
# autolabel(bar2)

plt.ylabel('Sales Amount and Return',fontweight="bold")
plt.xlabel('RSMTR Name',fontweight="bold")
plt.title('Sales Evaluation - Developed by BM-Ashik',fontweight="bold")
plt.xticks(bar_index, data['RSMTR'])
# plt.xticks(bar_index + bar_width / 2, sales_person)

# plt.legend(['30 Days Return', 'YesterDay Sales'])
ax.legend(labels=(['30 Days Return', 'YesterDay Sales']), loc='upper center', bbox_to_anchor=(0.5, -0.25),
          fancybox=True, shadow=True, ncol=5)  # legend placed at lower right


plt.tight_layout()
plt.show()
