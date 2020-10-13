import numpy as np
import pandas as p
#############key point ot know in pandas
df = p.DataFrame(np.random.randn(1000,2),columns=['A','B'])
print (df)


# to list first 30 rows in a dataframe to a temp dataframe
temp_datset = df.ix[0:30]
###############
# Series
list1 =[1,2,3]
labl_l = ['a','b','c']
dict1 = {'a':1,'b': 2,'c':3,'d':4}
print (p.Series(data = list1 , index = labl_l))
print (dict.fromkeys(labl_l,list1))
print (p.Series(dict1))

# adding 2 series
print (p.Series(data = list1 , index = labl_l) + p.Series(dict1))


# DataFrames
df1 = p.DataFrame(np.random.randn(5,4),['r1','r2','r3','r4','r5'],['c1','c2','c3','c4'])
print (df1)
print (df1[['c1','c2']])
# Adding a new column
df1['c5'] = df1['c1'] + df1['c2']
print (df1)


#print (df1.drop('r2',axis = 0, inplace= True))  for dropping rows
#print (df1.drop('c5',axis = 1, inplace= True))  for dropping columns
#print (df1)

print (df1.loc[['r1','r3'],['c1','c3']])

print (df1[df1['c1']> 0])
print (df1[df1['c1']> 0][['c2','c3']])

print (df1[(df1['c1']> 0) & (df1['c2']>0)])

## Handing null in dataframes
d= {'a':[1,2,3],'b':[5,6,np.NaN],'c':[np.NaN,np.NaN,6]}
df2= p.DataFrame(d)
print (df2)
print (df2.dropna())  # will drop all rows having any NaN value
print (df2.dropna(axis= 1)) # will drop all columns having any NaN value
print (df2.dropna(thresh=2)) # will drop if rows not having atleast 2 non null values
df3= p.DataFrame(d)
print (df3.fillna(value=' '))

### GroupBY function
d = {'company':['GG','GG','AMZ','AMZ','FB'],'name':['a','b','c','d','e'],'salary':[100, 200, 300,400,500]}
df3 = p.DataFrame(d)
print (df3)
mycomp = df3.groupby('company')
print (mycomp.sum().loc['FB'])
print (df3.groupby('company').sum().loc['GG'])
# use describe method
df4 = (df3.groupby('company').describe().transpose())
print (df4["AMZ"]) 
print (df4["AMZ"].iloc[0])

# Joining dataframes
a = {'join_id':[1,2,3,4], 'name':['saranya','karthi','harshith','meera']}
table_a = p.DataFrame(a)
b ={'join_id':[1,2,3,4],'salary':[1000,2000,3000,3000]}
table_b = p.DataFrame(b)
print (p.merge(table_a,table_b,how='inner',on ='join_id'))

############
# Points from Training
# df.loc[row_condition, columns selection] to get the rows
# to drop any row based on row_index(eg: 2), df.drop(2)
# after dropping df.reset_index(drop=True) -> drops old index and create new one
# df.drop(columns=["column1"])