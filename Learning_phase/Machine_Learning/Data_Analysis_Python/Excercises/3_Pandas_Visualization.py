import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



############################################################
x = np.arange(-10, 11)
## takes values of -10 to 11 in x list

plt.figure(figsize=(12,6))
T#he figsize=(12, 6) argument sets the width of the figure to 12 inches and the height to 6 inches. This ensures that your plot will be larger and more readable.

plt.title('My Nice Plot')
#It Defines the table name

plt.plot(x, x ** 2)
plt.plot(x, -1 * (x ** 2))
# plt.plot(x, y) --> Both draws in a single plot




############################################################
plt.figure(figsize=(12, 6))
plt.title('My Nice Plot')


plt.subplot(1, 2, 1)  # rows, columns, panel selected
##subplot[rows, columns, whichone is selected]
# if there is 2 rows 2 columns...
#plt.subplot(2, 2, 2) selects the second subplot (top-right corner).
#plt.subplot(2, 2, 3) selects the third subplot (bottom-left corner).

plt.plot(x, x ** 2)
plt.plot([0, 0, 0], [-10, 0, 100])
#plots [x, y]

plt.legend(['X^2', 'Vertical Line'])
#plots legend inside the figure
plt.xlabel('X')
plt.ylabel('X Squared')
#names the x-coordinate and y-coordinate 


plt.subplot(1, 2, 2) ##second fig selected
plt.plot(x, -1 * (x ** 2))
plt.plot([-10, 0, 10], [-50, -50, -50])
plt.legend(['-X^2', 'Horizontal Line'])
plt.xlabel('X')
plt.ylabel('X Squared')

##############################################################


# OOP Interface 

fig, axes = plt.subplots(figsize=(12, 6))
#The Figure object that holds all the plot elements (axes, titles, legends, etc.).
# We can use fig to manipulate the whole figure, such as saving it, adjusting its layout, etc.

# The Axes object, where you actually plot your data.
# Axes represents a plot within the figure. If we have multiple subplots, this will be an array of axes.


axes.plot(x, (x ** 2), color='red', linewidth=3,marker='o', markersize=8, label='X^2')
axes.plot(x, -1 * (x ** 2), 'b--', label='-X^2')
# axes.plot(x,y, & other attributes)

axes.set_xlabel('X')
axes.set_ylabel('X Squared')

axes.set_title("My Nice Plot")

axes.legend()

fig


###################################################

fig, axes = plt.subplots(figsize=(12, 6))

axes.plot(x, x + 0, '-og', label="solid green")
axes.plot(x, x + 1, '--c', label="dashed cyan")
axes.plot(x, x + 2, '-.b', label="dashdot blue")
axes.plot(x, x + 3, ':r', label="dotted red")
#plotting with diff colors and dashes
axes.set_title("My Nice Plot")

axes.legend()
#legend would automatically says solid green, dotted red etc if not give

######################################################

#It creates a simple fig with 1 axis that plots (1,1) (2,2) (3,3)
plot_objects = plt.subplots()
fig, ax = plot_objects
ax.plot([1,2,3], [1,2,3])
plot_objects

#######################################################

#It creates 2 rows 2 col ; so four axis and the complete figsize is 14l 6w
plot_objects = plt.subplots(nrows=2, ncols=2, figsize=(14, 6))
fig, ((ax1, ax2), (ax3, ax4)) = plot_objects
plot_objects

ax4.plot(np.random.randn(50), c='yellow')
ax1.plot(np.random.randn(50), c='red', linestyle='--')
ax2.plot(np.random.randn(50), c='green', linestyle=':')
ax3.plot(np.random.randn(50), c='blue', marker='o', linewidth=3.0)

fig #This draws the figure

####################################################

# Scatter Plot
N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (20 * np.random.rand(N))**2  # 0 to 15 point radii

plt.figure(figsize=(14, 6))
plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Spectral')
plt.colorbar()
plt.show()

#################################################################

fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(1,2,1)
plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Pastel1')
plt.colorbar()

ax2 = fig.add_subplot(1,2,2)
plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Pastel2')
plt.colorbar()

plt.show()

###########################################################


# Histograms

plt.subplots(figsize=(12, 6))

plt.hist(values, bins=100, alpha=0.8,
          histtype='bar', color='steelblue',
          edgecolor='green')
plt.xlim(xmin=-5, xmax=5)

plt.show()

fig.savefig('hist.png')

##########################################################3

