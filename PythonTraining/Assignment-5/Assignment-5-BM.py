# B.M. ASHIK MAHMUD
# Assignment 5

import pandas as pd
import pyodbc as db
from matplotlib import pyplot as plt
import numpy as np

## Create Database connection ---------

# connection = db.connect(
#     'DRIVER={SQL SERVER};'
#     'SERVER=137.116.139.217;'
#     'DATABASE=ARCHIVESKF;'
#     'UID=sa;PWD=erp@123')
# query = """
#             DECLARE @Thisday CHAR(8) = CONVERT(varchar(8), dateAdd(day,-1,getdate()), 112)
#             DECLARE @lastday CHAR(8) = CONVERT(varchar(8), dateAdd(DAY,-2,getdate()), 112)
#             DECLARE @thismonth CHAR(6) = CONVERT(varchar(6), dateAdd(MONTH,0,getdate()-30), 112)
#             select top 10 RSMTR as RSMTR,
#             SUM(case when TRANSDATE = @Thisday then EXTINVMISC END)  as YesterdaySales,
#             SUM(case when TRANSDATE = @lastday then EXTINVMISC END) as BeforeTwodaysSales,
#             SUM(case when transtype=2 and left(transdate,6) = @thismonth then EXTINVMISC*(-1) END) as ReturnVal
#             from OESalesDetails
#             group by RSMTR
#             order by  YesterdaySales desc,   BeforeTwodaysSales desc, ReturnVal DESC
# """
# data = pd.read_sql_query(query, connection)
# # print(type(data))
# data.to_csv('assignment5bm.csv',index=False)
# print('Data Saved')

data = pd.read_csv('F:/PythonProject/Training/assignment5bm.csv')
print(data['YesterdaySales'])