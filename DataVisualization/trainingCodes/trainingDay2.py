import matplotlib.pyplot as plt
import numpy as np
import pyodbc as db
import pandas as pd
connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=10.168.2.241;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp')
cash_drop_df = pd.read_sql_query("""
    Select case 
   when Days_Diff between 0 and 3  THEN '0 - 3 days' 
   when Days_Diff between 4 and 10  THEN '4 - 10 days'
   when Days_Diff between 11 and 15  THEN '11 - 15 days'  
   else '16+ Days' end  as AgingDays,
   --OUT_NET
   Sum(OUT_NET) as Amount 
   from 
      (select INVNUMBER,INVDATE,
      CUSTOMER,TERMS,MAINCUSTYPE,
      datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 as Days_Diff,
      OUT_NET from [ARCOUT].dbo.[CUST_OUT] 
      where [ARCOUT].dbo.[CUST_OUT].AUDTORG = 'RNGSKF' and TERMS='Cash') as TblCredit
      group by 
         case 
            when Days_Diff between 0 and 3 THEN '0 - 3 days'
            when Days_Diff between 4 and 10  THEN '4 - 10 days'
            when Days_Diff between 11 and 15  THEN '11 - 15 days'
             else '16+ Days' end 
                        """, connection)
width = 0.75
AgingDays = cash_drop_df['AgingDays']
y_pos = np.arange(len(AgingDays))
performance = cash_drop_df['Amount']
fig, ax = plt.subplots()
rects1 = plt.bar(y_pos, performance, width, align='center', alpha=0.9, color='#fd00ff')
# fig.set_size_inches(12.80, 4.8)
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.001 * height,
                '%d' % int(height),
                ha='center', va='bottom')
autolabel(rects1)
plt.xticks(y_pos, AgingDays, fontweight='bold')
# plt.yticks(np.arange(0, 2001, 200))
plt.xlabel('Aging Days', color='black', fontsize=14, fontweight='bold')
plt.ylabel('Amount', color='black', fontsize=14, fontweight='bold')
plt.title('Aging Days - Cash Drop', color='black', fontweight='bold', fontsize=18)
plt.savefig('bb.png')
# plt.close()
#plt.show()