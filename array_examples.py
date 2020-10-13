from array import *

# Print a simple array
array1 =array('i',[123,45,56,667,89,123,67,123])
print ("Printing indexes of array elements")
for i in array1:
	print ("values of array  {} is on index {}".format(i, array1.index(i)))

# Append a value to the array
array1.append(98)
print ("appenede 98 to the array",array1)


# Reversing the array
array1.reverse()
print ("Reversed array ",array1)


# Sorting array
#array1.sort()
#print ("Sorted array ",array1)

# Length of bytes of one array item
print ("Length of bytes of one array item ",array1.itemsize)

#memory buffer of array 
print ("memory buffer of array ", (array1.buffer_info()[1]) * array1.itemsize)

print ("123 occured times: ",array1.count(123))

array1.remove(45)

# Inserting elements at particular position
print ("Old array",array1)
array1.insert(2,100)
print ("Newly inserted 100 at position 3" ,array1)


# converting lists to array
list1 = [23,11,45,67,34,90]
array1 = array('i',list1)
print (array1)


# Converting array to list
list2 = array1.tolist()
print ("List derived from array ",list2)

