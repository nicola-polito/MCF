# SUBPLOTS EXAMPLES

import matplotlib.pyplot as plt
import numpy as np

#example 1
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)
fig, axs= plt.subplots(2, 2)
fig.suptitle('Vertically stacked subplots')
axs[0,0].plot(x,y)
axs[0,0].set_title('Axis[0,0]')
axs[0,1].plot(x,y,'tab:orange')
axs[0, 1].set_title('Axis [0, 1]')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 0].set_title('Axis [1, 0]')
axs[1, 1].plot(x, -y**2, 'tab:red')
axs[1, 1].set_title('Axis [1, 1]')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

for ax in axs.flat:
    ax.label_outer()

#for ax in fig.get_axes():
 #   ax.label_outer()

#example 2
#you can use sharex or sharey to align the horizontal or vertical axis
fig, (ax1, ax2)= plt.subplots(2, sharex=True)
fig.suptitle('Aligning x-axis using sharex')
ax1.plot(x,y)
ax2.plot(x+1, -y)
#Tick labels of inner Axes are automatically removed by sharex and sharey

#example 3
#remove the unused empty space between subplots
fig=plt.figure()
gs= fig.add_gridspec(3, hspace=0)
axs = gs.subplots(sharex=True, sharey=True)
fig.suptitle('Only One object divided in subplots')
axs[0].plot(x,y**2)
axs[1].plot(x, 0.3*y, 'o')
axs[2].plot(x,y,'+')

for ax in axs:
    ax.label_outer()
#apart from True and False, both sharex and sharey accept the values 'row' and 'col' to share th values only for rows or columns

#example 4
'''
If you want a more complex sharing structure, you can first create the grid of axes with no sharing, and then call axes.
Axes.sharex or axes.Axes.sharey to add sharing info a posteriori.
'''

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 0].set_title("main")
axs[1, 0].plot(x, y**2)
axs[1, 0].set_title("shares x with main")
axs[1, 0].sharex(axs[0, 0])
axs[0, 1].plot(x + 1, y + 1)
axs[0, 1].set_title("unrelated")
axs[1, 1].plot(x + 2, y + 2)
axs[1, 1].set_title("also unrelated")
fig.tight_layout()

#example 5 (POLAR AXES)
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
ax1.plot(x, y)
ax2.plot(x, y ** 2)

plt.show()