import pandas as pd
df1 = pd.read_json('/Users/skarthi/Documents/Python_Scripts/Data/sample_json.json') 
#print (df1.head())

# get the users with max count

df2 = (df1[df1['completed']])
#print (df2.head())
#print ('Max user ')
print (df2['userId'].value_counts())

list1 = [{'userid':3,'id':1,'completed':True},{'userid':3,'id':2,'completed':True},
{'userid':2,'id':3,'completed':True},{'userid':4,'id':1,'completed':True}]
n_list=[]
for i in range(0,len(list1)):
  n_list.append(list1[i]['userid'])
print (n_list)
output = (max(n_list,key=n_list.count))
print (output)




