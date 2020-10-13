import copy
list1 = [12,13,14]
print (list1)

print (list1[0],"/n",list1[1])

list1.sort(reverse= True)
print ("Reversing the list", list1)

print (" multiplying each items by 2's like 12*2, 13*4,14*16")
output_list = list()
j = 2
for i in list1:
	output_list.append(i*j)
	j = j*j
print (output_list)

list3 = [345,99,8475,11111]
print ("Sorting the list by sum of digits in the number")
def sum_digits(a):
	sum = 0
	while(a):
		sum = sum+ (a%10)
		a = a/10
		
	return sum

list3.sort(reverse =True,key=sum_digits)

print (list3)

################Sorting alphabetically
list4 =["apples","orange","banana"]
list4.sort()
print (list4)
###############Sorting list based on length of text
list5 = ["asd","riutr","hfdd","dfhsjhfs"]

def length(a):
	return len(a)

list5.sort(reverse=True,key = length)
print (list5)

############### sum up all values in the list
list6 =[23,34,78,90]
sum= 0
for i in list6:
	sum= sum+i
print ("Sum of vales in the list is %d",sum)

################### Grouping into seperate list based on even or odd numbers
list7 =[56,23,43,56,72]
even_list=[]
odd_list=[]


##################Grouping into different list based on whether index is odd or even

################# List reverse printing
list8 =["tty","uiui","hh","hiu"]
print ("printing last value in list",list8[-1])
print ("printing last but second value",list8[-2])
list9 =copy.copy(list8)
list9.reverse()
print ("reversed list",list9)


############# Mixed lists
list9 =[67,"hjhhj",[1,2,3]]
print ("printing mixed list",list9)
list9[2].append(4)
print ("added 1 element to the inner list",list9[2])

############## Nested Lists
############### combining nested lists to one list
list10 = [[2,3,4],[54,343,11],[66,45,22]]
print (list10)
list= list10[0] + list10[1] + list10[2]
print ("Printing lists within lists", list)

############### Slicing lists into different lists based on condition(even or odd)
list1 = [23,44,46,77,89,110]
even_list =[]
odd_list =[]
for i in list1:
	if i%2 == 0:
		even_list.append(i)
	else:
		odd_list.append(i)
print ("Even number list",even_list)
print ("Odd Number list",odd_list)

################ finding biggest number or string in list
list =[232,2323,434]

print ("Biggest number in the list",max(list))
list2 = ["hfsjh","sdjksj","abcsfeeo"]
list3 =copy.copy(list2)
print (list3)
#list3.sort()
#print ("LOngest string in the list",(list3[-1]))

################finding biggest of 2 lists by items count
print ("Displaying bigger list")
list1 = [34,56,67,678]
list2 = [232,344,55,234,1112,345]
if list1 > list2:
	print (list1)
else:
	print (list2)
################finding biggest by sum of items in the list
print ("finding biggest by sum of items in the list")
list1 = [34,56,67,678]
list2 = [232,344,55,234,1112,345]
sum1= 0
sum2 = 0
for i in list1:
	sum1 = sum1 + i
for j in list2:
	sum2 = sum2 + j


if sum1 > sum2:
	print ("Biggest sum of items in list is list1 ",sum1)
else:
	print ("Biggest sum of items in list is list2 ",sum2)

################finding biggest list by adding all the digits
print ("finding biggest by sum of items by adding all the digits")
list1 = [34,56,67,678]
list2 = [232,344,55,234,1112,345]
sum1 = 0
for i in list1:
	while(i):
		sum1 = sum1 + (i%10)
		i = i/10
print ("Adding all the digists in 1st list",sum1)
sum2 = 0
for i in list2:
        while(i):
                sum2 = sum2 + (i%10)
                i = i/10
print ("Adding all the digists in 2nd list",sum2)
if sum1 > sum2:
	print ("1st list is bigger")
else:
	print ("2nd list is bigger")

#################Concatenate 2 lists
print ("Concatenate 2 lists")
list1= [12,1232,242]
list2=[23,44,32]
list1= [12,1232,242]
list2=[23,44,32]
concat_list = list1+list2
print (concat_list)

###############

# finding the number of occurence of a number in list
print ('finding the number of occurence of a number in list')
list1 =[34,3,34,5,3,34]
print (max(list1,key=list1.count))

list2 =["abc",1,"a",[5,6],"abc"]
print (max(list2,key=list2.count))

print ("Sort by the number of occurences")

print (sorted(list1,key = list1.count))

######################
list1 = [34,11,67,89]
list2 = [23,25,90,2,67]
list3 = list1 +list2

print (list3)


list1 =[34,56,11,32]
list2 = [78,11,2,44,78]
list3 =[]
if list1 > list2:
    n = (len(list1))
else:
    n = (len(list2))

for i in range(0,n-1):
    x = list1[i]
    y = list2[i]
    list3.append(x)
    list3.append(y)

z= list2[n-1]
list3.append(z)
print (list3)

#output: [34, 78, 56, 11, 11, 2, 32, 44, 78]

# reversing the list
print ("Reversing the list")
list1 =[1,2,3,4]
n = len(list1)
rev_list =[]
for i in list1:
	rev_list.append(list1[n-1])
	n = n -1
print ("Reversed list is {}".format(rev_list))

# sum of 2 numbers should be 101 , find the 2 numbers
list1 =[23,12,89,55,12]
list2 = copy.copy(list1)
print ("Copied list",list2)

for i in list1:
	for j in list2:
		if i+j==101:
			a= i
			b=j
			break

print ("two numbers which will add up to 101 ", a,b)


## converting Int list values to string values
list1 =[1,2,3,4]
results =[]
results = list(map(str,list1))
print (results)



## sorting list without using sort fn

list1 =[7,3,1,2,5]
n = len(list1)
x = 0
for i in range(0,n):
        x = i+ 1
        for j in range(x,n):
                if list1[i] > list1[j]:
                        temp = list1[j]
                        list1[j] = list1[i]
                        list1[i] = temp
print (list1)
print ("casting str list to int")
list_str =['1','2','3','4','5']
print (list_str)
list_int = list(map(lambda x: int(x), list_str))
print (list_int)

