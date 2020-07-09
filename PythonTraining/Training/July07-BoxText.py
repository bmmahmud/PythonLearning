import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Box 1
left, width = 0.0, 0.24
bottom, height = 0,1
right = left + width
top = 1
fig = plt.figure(figsize=(12,2))
ax = fig.add_axes([0,0,1,1])

#----------------------- remove border from the figure
for item in [fig,ax]:
    item.patch.set_visible(False)
    fig.patch.set_visible(False)
    ax.axis('off')


#---------------------------------
p = patches.Rectangle( (left,bottom),width,height,color = '#f0a500')
ax.add_patch(p)
# plt.show()

kpi_lable = 'Return'
return_p = '1.2%'
ax.text(0.5 * (left + right), 0.55 * (bottom + top), kpi_lable,
        ha = 'center',va = 'center',
        fontsize=24, color='black',
        transform = ax.transAxes)

ax.text(0.5 * (left + right), 0.3 * (bottom + top), return_p,
        ha = 'center',va = 'center',
        fontsize=24, color='red',
        transform = ax.transAxes)
#
# # Box 2
left, width = 0.25, 0.24
bottom, height = 0,1
right = left + width
top = 1

p = patches.Rectangle((left,bottom),width,height,color = '#21bf73')
ax.add_patch(p)
# plt.show()

kpi_lable = 'MTD'
return_p = '40%'
ax.text(0.5 * (left + right), 0.55 * (bottom + top), kpi_lable,
        ha = 'center',va = 'center',
        fontsize=24, color='black',
        transform = ax.transAxes)

ax.text(0.5 * (left + right), 0.3 * (bottom + top), return_p,
        ha = 'center',va = 'center',
        fontsize=24, color='red',
        transform = ax.transAxes)

# # Box 3
left, width = 0.50, 0.24
bottom, height = 0,1
right = left + width
top = 1

p = patches.Rectangle((left,bottom),width,height,color = '#654062')
ax.add_patch(p)
# plt.show()

kpi_lable = 'MTD'
return_p = '40%'
ax.text(0.5 * (left + right), 0.55 * (bottom + top), kpi_lable,
        ha = 'center',va = 'center',
        fontsize=24, color='black',
        transform = ax.transAxes)

ax.text(0.5 * (left + right), 0.3 * (bottom + top), return_p,
        ha = 'center',va = 'center',
        fontsize=24, color='red',
        transform = ax.transAxes)
# Save Images
# # Box 4
left, width = 0.75, .24
bottom, height = 0,1
right = left + width
top = 1

p = patches.Rectangle((left,bottom),width,height,color = '#ff9c71')
ax.add_patch(p)
# plt.show()

kpi_lable = 'MTD'
return_p = '40%'
ax.text(0.5 * (left + right), 0.55 * (bottom + top), kpi_lable,
        ha = 'center',va = 'center',
        fontsize=24, color='black',
        transform = ax.transAxes)

ax.text(0.5 * (left + right), 0.3 * (bottom + top), return_p,
        ha = 'center',va = 'center',
        fontsize=24, color='red',
        transform = ax.transAxes)

plt.savefig('BoxText.png')

plt.show()


