# B.M. ASHIK MAHMUD
#  cumulative

import pandas as pd
import pyodbc as db
from matplotlib import pyplot as plt
import numpy as np

## Create Database connection ---------

connection = db.connect(
    'DRIVER={SQL SERVER};'
     'SERVER=137.116.139.217;'
    #'SERVER=10.168.2.241;'
    'DATABASE=ARCHIVESKF;'
    'UID=sa;PWD=erp@123'
    #'UID=sa;PWD=erp'
    )
# salessql = """
#         SELECT
#         LEFT(TRANSDATE, 6) AS MONTHS
#         ,SUM(EXTINVMISC) AS SALES
#         FROM OESalesDetails
#         where
#         (TRANSDATE between
#         convert(varchar(8),DATEADD(YEAR, DATEDIFF(YEAR, 0, GETDATE()), 0),112) ---First day of the YEAR
#         AND
#         convert(varchar(8),DATEADD(day,-1,DATEADD(MM, DATEDIFF(MM,0,GETDATE()),0)),112) -- Last day of last month
#         )
#         GROUP BY LEFT(TRANSDATE, 6)
#         ORDER BY LEFT(TRANSDATE, 6)
# """
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

# sales = pd.read_sql_query(salessql, connection)
target = pd.read_sql_query(targetsql, connection)
# print(sales)
# print(target)

# --------- GRAPH CODE BELOW
# # some fake data
# data = target['TARGETS']
# series = pd.Series(data)
#
# # calling method
# cumsum = series.cumsum()
# # evaluate the histogram
# values, base = np.histogram(cumsum, bins=40)
# #evaluate the cumulative
# cumulative = np.cumsum(values)
# # plot the cumulative function
# plt.plot(base[:-1], cumulative, c='blue')
# # #plot the survival function
# # plt.plot(base[:-1], len(data)-cumulative, c='green')
#
# plt.show()


#----------------------------
# data = target['TARGETS']
# series = pd.Series(data)
#
# # calling method
# cumsum = series.cumsum()
# # evaluate the histogram
# values, base = np.histogram(cumsum, bins=40)
# #evaluate the cumulative
# cumulative = np.cumsum(values)
#
# np.random.seed(19680801)
#
# mu = 200
# sigma = 25
# n_bins = 50
# x = cumulative
#
# fig, ax = plt.subplots(figsize=(8, 4))
#
# # plot the cumulative histogram
# n, bins, patches = ax.hist(x, n_bins, density=True, histtype='step',
#                            cumulative=True, label='Empirical')
#
# # Add a line showing the expected distribution.
# y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
#      np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
# y = y.cumsum()
# y /= y[-1]
#
# ax.plot(bins, y, 'k--', linewidth=1.5, label='Theoretical')
# # tidy up the figure
# ax.grid(True)
# ax.legend(loc='right')
# ax.set_title('Cumulative step histograms')
# ax.set_xlabel('Annual rainfall (mm)')
# ax.set_ylabel('Likelihood of occurrence')
#
# plt.show()