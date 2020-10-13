import numpy as np
import pandas as pd
import seaborn as sns
%matplotlib inline


device_ds = pd.read_csv('/Users/skarthi/Documents/Python_Scripts_Basics/Data/device_data.csv')
print (device_ds.head())

# Distribution Plot , historgram on price column
sns.distplot(device_ds['price'],kde=True,bins=10) 
# if we include "kde=False", then curved line disappers
# KDE IS KERNEL DESNITY DISTRIBUTION

# KDE plot
sns.kdeplot(device_ds['price'])

# Jointplot , is simlar as scatter plot
sns.jointplot(x='device_cnt',y='price',data=device_ds,kind='kde') 
# for 'kind' variable , we can select hex for hexagon pattern instead of cirle,
# or we can select 'reg' for regression pattern, shows like linear regression line
# or we can write 'kde', shows like oval pattern 

# pairplot kinds of shows all the possible combination of metrics 
# in the data to show its relationships
sns.pairplot(device_ds,hue='emp_type') # hue is like color by for the pair plot
# palette ='coolwarm' is used to choose the legend color of hue(emp_type)


##############
# categorical plots
# Bar plots
sns.barplot(x='emp_type',y='price',data=device_ds)

# 5. countplots  
sns.countplot(x='Sex',data=t_ds)

# 6. Heatmap
sns.heatmap(t_ds.corr(),cmap='coolwarm')
plt.title('titanic.corr() heatmap')

# 7. PairGrid
g = sns.FacetGrid(data=t_ds,col='Sex')
g.map(sns.distplot,'Age')