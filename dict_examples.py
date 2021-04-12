import copy
dict1 = {"name" :"saran","age" : 30, "city" :"fremont"}
print (f'Sample dictionary is {dict1}')

print (dict1["name"])
print ("Displaying columns in Dictionary")

for i in dict1:
	print ("Value for {} : {}".format(i,dict1[i]))

dict1["company"] ="gg"
print (dict1)
print ("Length of dictionary is {}".format(len(dict1)))
dict1.pop("company")
print (dict1)

dict2 = dict1.copy()

print ("displaying copied dict {}" .format(dict2))

columns = ("emp_id","emp_name","salary")
values = 0

dict1 = dict.fromkeys(columns,values)
print ("New Dictionary is {}".format(dict1))
dict1.update({"emp_id" : 1})
print ("Upadted dictionary is {}".format(dict1))
dict2 = {"name" :"saran","age" : 30, "city" :"fremont"}
#test_list =copy.copy(list(dict2.items()))
#print ("printing dictinary as list",list(dict2.items()))
#print ("Copying dictionary to list",test_list)
#print ("printing dictinary as list & showing 1st element",list(dict2.items())[0][0])

person = {"name":"skarthi","age": "30","spouse":"karthi","children":["harshith","meera"],"pets":{"cat":"merry","dog":"puppy"}}
print ("printing each values in the dictionary")
print (person["name"])
print (person["children"])
print (person["children"][0])

print (person["pets"]["cat"])

dict1= {"a":1,"b":2,"c":3,"d":4}

(dict1.update(b=22))
print (dict1)
print (dict1.keys())
print (dict1.values())

#print (list(dict1.items()))

#---------------
# printing values in dictionary 0:0, 1:1,2:4,3:9
dict2= {}

for i in range(6):
	dict2[i] = i*i

print (dict2)


# printing  {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

dict2.clear()

for i in range(9):
	if i%2 != 0:
		dict2[i+1] = (i+1) *(i+1)
		i = i+1

print (dict2)
	
########## to know whether a key present in dictionary

print(3 in dict2)

print(4 in dict2)

dict3 ={1:34,3:11,2:45,6:23,4:90}

print("Sorting dictionary {}".format(sorted(dict3)))
print("length of dictionary",len(dict3))

########## Nested Dictionary
dict1 = {1:{"name":"abc","age":30,"gender":"male"},2:{"name":"dfg","age":11,"sex":"female"}}

print ("looping in the nested dictionary")

for i,values  in dict1.items():
	print ("row_id is {}".format(i))
	for x in values:
		print ("value for {} is {}\n".format(x,values[x])) 

################## appending 2 dictionries

dict3 ={1:34,3:11,2:45,6:23,4:90}
dict4 ={10:334,23:211,22:345,36:231,24:790}

for i in dict4:
	dict3[i]=dict4[i]

print ("Conatenated dictionary list is {}".format(dict3))


columns = ("emp_id","emp_name","salary")
values = 0

dict1 = dict.fromkeys(columns,values)
print ("New Dictionary is {}".format(dict1))
dict1.update({"emp_id" : 1})
print ("Upadted dictionary is {}".format(dict1))
dict2 = {"name" :"saran","age" : 30, "city" :"fremont"}
test_list =copy.copy(list(dict2.items()))
print ("printing dictinary as list",list(dict2.items()))
print ("Copying dictionary to list",test_list)
print ("printing dictinary as list & showing 1st element",list(dict2.items())[0][0])









