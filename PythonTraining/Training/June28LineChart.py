from matplotlib import pyplot as plt
#
# x = ['A','B','C','D','E']
# y = [24,48,30,50,45]
# # x = (data.AUDTORG.tolist())
# plt.plot(x,y,color='red')
#
# plt.xlabel("Name")
# plt.ylabel("Marks")
# plt.title('Line Chart')
# plt.show()


# multiple lines
x = ['A','B','C','D','E']
y = [24,48,30,50,45]
z = [12,41,24,54,21]

fig, ax = plt.subplots()
plt.plot(x,y,color='red')
plt.plot(x,z,color='blue')

ax.legend(labels =('Math','English'),loc='best')
# plt.xlabel("Name", color = 'black',fontsize=14,fontwidth=20)

plt.savefig('figure.png')
plt.xlabel("Name")
plt.ylabel("Marks")
plt.title('Line Chart')
plt.show()