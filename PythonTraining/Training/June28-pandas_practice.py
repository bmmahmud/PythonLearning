# # Training Day 4 - 28 June
import pandas as pd
import pyodbc as db
#
# ## Create Database connection ---------
#
# connection = db.connect(
#     'DRIVER={SQL SERVER};'
#     'SERVER=137.116.139.217;'
#     'DATABASE=ARCHIVESKF;'
#     'UID=sa;PWD=erp@123')
# query = """select top 1000 * from OESalesDetails"""
# data = pd.read_sql_query(query,connection)
# # print(type(data))
# data.to_csv('sales_data.csv',index=False)
# print('Data Saved')


#
# # Get Data from csv Files ----------
data = pd.read_csv('F:/PythonProject/Training/sales_data.csv')
print(data.head())

# print(data.head(4))
# print(type(data))

# # Create DataFrame -
# df = pd.DataFrame({'Yes':[10,20],'No':[40,30]})
# print(df)
#
# df1 = pd.DataFrame({'Bob': ['I like it.','It was awful.']}),
#                     'sure'

# print(data.columns) # All column name

# print(data.shape) # rows, columns of dataFame

# # print(data.AUDTORG)
# # print(data['AUDTORG'])
# print(data.AUDTORG.iloc[0])
#
# ## condition
#
# rang= data.loc[(data.AUDTORG == 'RNGSKF')]
# print(rang)
