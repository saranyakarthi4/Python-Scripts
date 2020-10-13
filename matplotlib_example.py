import matplotlib.pyplot as plt
import numpy as np
from random import sample

x_axis = np.linspace(0,5,11)
print (x_axis)
#y_axis = x_axis ** 2
y_axis = np.linspace(2,20,11)
print (y_axis)
# Line chart
plt.plot(x_axis,y_axis)  # print (plt.show()) not needed actually
plt.xlabel("people count")
plt.ylabel("ratio %")
plt.title ("people # vs Ratio %")

# subplots : to create 2 charts next to each other
plt.subplot(1,2,1)  # subplt(no of rows, no of columns, plot number(1 or 2 or 3 etc))
plt.plot(x_axis,y_axis,'b')
plt.xlabel("chart 1")

plt.subplot(1,2,2)
plt.plot(y_axis, x_axis, 'r')
plt.xlabel("chart2")


#object oriented methods
# reason for uisng Obj oriented method / figure is it creates placeholder for charts
# so we can create multiple charts and place any objects in 100% canvas/placeholder
fig1 = plt.figure()
axes = fig1.add_axes([0.1,0.1,0.8,0.8]) # add_axes(10% from left, 10% from bottom, 80% width, 80% height)
axes.plot(x_axis,y_axis)
axes.set_xlabel("X axis")
axes.set_ylabel("Y axis")
axes.set_title("chart using Obj Oriented Methods")

axes2 = fig1.add_axes([0.2,0.6,0.25,0.25])
axes2.plot(y_axis,x_axis)

fig1,axes = plt.subplots(nrows= 1, ncols= 2) # creates 4 charts , u could specify figsixe also here
axes[0].plot(x_axis,y_axis)
axes[0].set_title ("1st chart")
axes[1].plot(x_axis,y_axis)
axes[1].set_title ("2nd chart")
plt.tight_layout()

### Figure Size , Aspect ratio and DPI
print ('Figure Size options')
fig = plt.figure(figsize=(3,2)) # figsize: size of figure in inches, dpi : optional dots/pixels per inch
axes= fig.add_axes([0,0,1,1])
# multiple line chart use same axes
axes.plot(x_axis,y_axis,label="line1")
axes.plot(y_axis,x_axis,label = "line2")
axes.legend(loc= 2) # LOCATION CODE can be 0 to 10, 0 means best, 1: upper right, 2 : upper left , 10: center etc
# or u can also use loc =(0.1,0.1) which means 10% from left , 10% from bottom of the figure
fig.savefig("/Users/skarthi/Documents/Python_Scripts_Basics/chartfig.png",dpi= 500)

fig1 = plt.figure()
axes = fig1.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x_axis,y_axis,color='green',linewidth=2,linestyle='--',marker='o',markersize=10,markerfacecolor='yellow',markeredgewidth= 0.5,markeredgecolor='blue')

# histogram
fig2 =plt.figure()
data = sample(range(1,1000),100)
plt.hist(data)

# Scatter Plots
fig3 =plt.figure()
plt.scatter(x_axis,y_axis)



