import numpy as np
import pandas as pd
import seaborn as sns
from pandas_datareader import data,wb
#import pandas.io.data as web
import datetime
import matplotlib.pyplot as plt
plt.style.use('ggplot')
%matplotlib inline

BAC= pd.read_csv('/Users/skarthi/Documents/Python_Scripts_Basics/Data/BAC.csv')
BAC['bank_name'] ='BAC'
BAC['change_pct'] = BAC['Close'].pct_change()

GS= pd.read_csv('/Users/skarthi/Documents/Python_Scripts_Basics/Data/GS.csv')
GS['bank_name'] ='GS'
GS['change_pct'] = GS['Close'].pct_change()

C= pd.read_csv('/Users/skarthi/Documents/Python_Scripts_Basics/Data/C.csv')
C['bank_name'] ='C'
C['change_pct'] = C['Close'].pct_change()

JPM= pd.read_csv('/Users/skarthi/Documents/Python_Scripts_Basics/Data/JPM.csv')
JPM['bank_name'] ='JPM'
JPM['change_pct'] = JPM['Close'].pct_change()

MS= pd.read_csv('/Users/skarthi/Documents/Python_Scripts_Basics/Data/MS.csv')
MS['bank_name'] ='MS'
MS['change_pct'] = MS['Close'].pct_change()

WFC= pd.read_csv('/Users/skarthi/Documents/Python_Scripts_Basics/Data/WFC.csv')
WFC['bank_name'] ='WFC'
WFC['change_pct'] = WFC['Close'].pct_change()

bank_stocks = pd.concat([BAC,GS,C,JPM,MS,WFC])
#print (bank_stocks.info())
print (bank_stocks['bank_name'].unique())
print (bank_stocks.head(3))

# 1. Max Close price for each bank
max_cls_pr = bank_stocks.groupby('bank_name').agg({'Close':'max'})
print (max_cls_pr)

# 2. create empty dataframe and update it with the % difference of 'Close' column for each day compared to prev day from each bank
returns = pd.DataFrame()
returns['Date']= BAC['Date']
returns['BAC_returns'] = BAC['change_pct']
returns['GS_returns'] = GS['change_pct']
returns['C_returns'] = C['change_pct']
returns['JPM_returns'] = JPM['change_pct']
returns['MS_returns'] = MS['change_pct']
returns['WFC_returns'] = WFC['change_pct']
returns.set_index(['Date'],inplace=True)

print (returns.head(4))

# 3. Print the max and minimum close price dates of each bank
print ('max and minimum close price dates of each bank')
print (returns.idxmin())
print (returns.idxmax())

# 4. print the stddev of returns for each bank
print ('std dev of each bank returns')
print (returns.std())

# 5. print the stddev of BAC for the year 2019
#x = returns.ix['2019-01-01':'2019-12-31'].std()  -- Not Working

# 6 Create a distplot of 2015 Returns for MS only
sns.distplot(returns['MS_returns'],color ='green',bins=30)

# 7. Create a line plot for 'close price for each bank
lineplot = bank_stocks.groupby('bank_name').count()
lineplot['Close'].plot(figsize=(12,4))
plt.tight_layout()

#8. Moving 30 day average growth
bank_stocks.set_index(['Date'],inplace=True)
print (bank_stocks.head(3))
#bank_stocks.ix['2019-01-01':'2019-12-31'].rolling(window=30).mean().plot() Not working

# video part 3
# heatmap to show the co-relation between stock of each bank
# candle plot
# simple moving average plot
