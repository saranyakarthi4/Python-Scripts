list1 = [45,12,89,34,9,6]
list1.sort()
#print list1 [6,9,12,34,45,89] to find 44
data = 45
i = 0
n= len(list1)
#print (n)
while (i < n):
	mid = int((i+n)/2) 
	print (list1[mid])
	if (list1[mid] == data):
		print ("match found at {} ".format(i))
		break
	elif (list1[mid] < data):
		i = mid- 1
	else:
		n = mid + 1	 
		print ("condi 3")




