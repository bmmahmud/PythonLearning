import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Box 1
left, width = 0.0, 0.19
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

kpi_lable = 'MHK'
return_p = '125K'
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
left, width = 0.20, 0.19
bottom, height = 0,1
right = left + width
top = 1

p = patches.Rectangle((left,bottom),width,height,color = '#21bf73')
ax.add_patch(p)
# plt.show()

kpi_lable = 'FRD'
return_p = '80K'
ax.text(0.5 * (left + right), 0.55 * (bottom + top), kpi_lable,
        ha = 'center',va = 'center',
        fontsize=24, color='black',
        transform = ax.transAxes)

ax.text(0.5 * (left + right), 0.3 * (bottom + top), return_p,
        ha = 'center',va = 'center',
        fontsize=24, color='red',
        transform = ax.transAxes)

# # Box 3
left, width = 0.40, 0.19
bottom, height = 0,1
right = left + width
top = 1

p = patches.Rectangle((left,bottom),width,height,color = '#fbc687')
ax.add_patch(p)
# plt.show()

kpi_lable = 'RNG'
return_p = '240K'
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
left, width = 0.60, .19
bottom, height = 0,1
right = left + width
top = 1

p = patches.Rectangle((left,bottom),width,height,color = '#ff9c71')
ax.add_patch(p)
# plt.show()

kpi_lable = 'MOT'
return_p = '180K'
ax.text(0.5 * (left + right), 0.55 * (bottom + top), kpi_lable,
        ha = 'center',va = 'center',
        fontsize=24, color='black',
        transform = ax.transAxes)

ax.text(0.5 * (left + right), 0.3 * (bottom + top), return_p,
        ha = 'center',va = 'center',
        fontsize=24, color='red',
        transform = ax.transAxes)
# # Box 5
left, width = 0.80, .19
bottom, height = 0,1
right = left + width
top = 1

p = patches.Rectangle((left,bottom),width,height,color = '#32e0c4')
ax.add_patch(p)
# plt.show()

kpi_lable = 'MIR'
return_p = '45K'
ax.text(0.5 * (left + right), 0.55 * (bottom + top), kpi_lable,
        ha = 'center',va = 'center',
        fontsize=24, color='black',
        transform = ax.transAxes)

ax.text(0.5 * (left + right), 0.3 * (bottom + top), return_p,
        ha = 'center',va = 'center',
        fontsize=24, color='red',
        transform = ax.transAxes)


plt.savefig('box.png')

plt.show()


