import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

ds_911 = pd.read_csv('/Users/skarthi/Documents/Python_Scripts_Basics/Data/911.csv')
print (ds_911.head(2))

# 1. Top 5 zipcodes
print (ds_911['zip'].value_counts().head(5))

# 2. Top 5 townships for 911 calls
print (ds_911['twp'].value_counts().head(5))

# 3. unique count of title codes
print ('unique count of titles are {}'.format(ds_911['title'].nunique()))

# 4. create new column 'reason' based on title 
ds_911['reason'] = ds_911['title'].apply(lambda title: title.split(':')[0])

# 5. all the possible reason
print (ds_911['reason'].value_counts())

# 6. Create a count plot using reason column
#############sns.countplot(x=ds_911['reason'])

# 7. What is the datatype of timestamp column and convert/new column for timesatmp
#print (type(ds_911['timeStamp'].iloc[0]))
#print (type(pd.to_datetime('2015-12-10 17:40:00')))

ds_911['new_timestamp'] = ds_911['timeStamp'].apply(lambda ts : pd.to_datetime(ts))

ds_911['hour']  = ds_911['new_timestamp'].apply(lambda x: x.hour)
ds_911['month'] = ds_911['new_timestamp'].apply(lambda x: x.month)
ds_911['day_of_week'] = ds_911['new_timestamp'].apply(lambda x: x.dayofweek)

# 8 . how to map the numbers of week_no of dataframe with another dictionary
wk_day_dict ={0:'monday',1:'tuesday',2:'wednesday',3:'thursday',4:'friday',5:'saturday',6:'sunday'}
ds_911['day_of_week1'] = ds_911['day_of_week'].map(wk_day_dict)

# 9. Create seaborn count plot for day of week column with color on reason
###########sns.countplot(x='day_of_week1',data=ds_911,hue='reason',palette='viridis')
###########plt.legend(bbox_to_anchor=(1.05,1),loc=2)

# 10. Create seaborn count plot for month column with color on reason
###########sns.countplot(x='month',data=ds_911,hue='reason',palette='viridis')
###########plt.legend(bbox_to_anchor=(1.05,1),loc=2)

# 11. line plot of 'lat' column
bymonth= (ds_911.groupby('month').count())
print (bymonth.head(2))
############bymonth['lat'].plot()

# 12. create lmplot to create linear fit model of number of calls per month
############sns.lmplot(x='month',y='twp',data=count_ds.reset_index())

# 13. create a date column from timestamp column
ds_911['date']= ds_911['new_timestamp'].apply(lambda x:x.date())
print (ds_911.head(2))

# 14. Plot for number of calls by date
byday = ds_911.groupby('date').count()
############byday['lat'].plot()
plt.tight_layout()        # to avoid overlapping of axis labels

# 15. create a line plot for Reason 'EMS'
reason_byday = ds_911[ds_911['reason']=='EMS'].groupby('date').count()
reason_byday['lat'].plot()
plt.tight_layout()
print (ds_911.info())
# 16. create haet map with weekdays and hours and color by zip column
hm= ds_911.pivot_table(index='day_of_week1',columns='hour',values='zip')
###########sns.heatmap(hm,cmap='coolwarm')

# create haet map with weekdays and hours and color by count of rows
dayhour=ds_911.groupby(by=['day_of_week1','hour']).count()['lat'].unstack()
##########plt.figure(figsize=(12,6))
##########sns.heatmap(dayhour)












