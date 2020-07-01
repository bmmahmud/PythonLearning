# Assignment - 3 Task - 2 [B.M. ASHIK MAHMUD]

from matplotlib import pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

Sales_person = ['Habib','Raihan','Rocky','Kabir']
Day1 = [30000,100000,40000,20000]
Day2 = [50000,10000,60000,100000]

fig, ax = plt.subplots()
plt.ylim(0,140000)
line1 = ax.plot(Sales_person,Day1, color='red',marker = 'o')
line2 = ax.plot(Sales_person, Day2, color='blue',marker = 'o')
plt.xticks(rotation=90, ha='right')

for Sales_person,Day1 in zip(Sales_person,Day1):
      plt.text(Sales_person, Day1, str(int(Day1/1000))+'k', weight='bold')

# for Sales_personB,Day2B in zip(Sales_person,Day2):
#       plt.text(Sales_personB, Day2B,str(Day2))

for Sales_personB,Day2B in enumerate(Day2):
    ax.text(Sales_personB, Day2B,(str(int(Day2B/1000))+'k'), ha="center", weight='bold')

# ax.legend(labels=('Sales Person', 'Day'), loc='best')  # legend placed at lower right
ax.legend(labels=('Sales', 'Day'), loc='upper center', bbox_to_anchor=(0.5, -0.25),
          fancybox=True, shadow=True, ncol=5)  # legend placed at lower right


plt.xlabel("Sales Person",  color='black', fontsize=14, fontweight='bold')
plt.ylabel("Amount", color='black', fontsize=14, fontweight='bold')
plt.title('Sales Performance', fontweight='bold', color='#3e0a75',  fontsize=18)
plt.tight_layout()
plt.savefig('Assignment-4-BMASHIK.png')
plt.show()
