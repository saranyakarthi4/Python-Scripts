import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')
%matplotlib inline

ds1 = pd.read_csv('/Users/skarthi/Documents/Python_Scripts_Basics/Data/df1.csv')
ds1.head(2)

# to oragnize the legend
ds1.plot.area(figsize=(12,3)).legend(loc='center left',bbox_to_anchor=(1.0, 0.5))

# line chart
ds1.plot.line(x=ds1['date_col'],y=ds1['A'])

# histogram
ds1['A'].hist(bins=20)
# other way to create histogran of column 'A' on dataset 'ds'
ds1['A'].plot(kind='hist',bins=30) # we can use "figsize= (12,3)"
# for color we can use "c='red' ", we use "alpha=0.5" to reduce the brighness of the chart
# or u can directly use ds1['A'].plot.hist()

ds2 = pd.read_csv('/Users/skarthi/Documents/Python_Scripts_Basics/Data/df2.csv')
ds2.head(2)

ds2.plot.area()
# similary as ds2.plot.bar(stacked=True)

# Scatter plot
ds1.plot.scatter(x='A',y='B')
# if we want the color_by by column c then "ds1.plot.scatter(x='A',y='B',c='C')
# if you want the colormap, the cmap='coolwarm', 
# for the size of markers then use 's=ds2['C']*100'
ds1.plot.scatter(x='A',y='B',c='C',cmap='coolwarm')

# box plot
ds1.plot.box()

# Scatter plot with hexagon shape
ds1.plot.hexbin(x='A',y='B',gridsize= 25)

#kde plot
ds2.plot.density()


