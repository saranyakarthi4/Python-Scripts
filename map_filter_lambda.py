# Creating own functions in python
def square(num):
    num1 = num **2
    return num1

x= square(5)
print(f'Square of 5 is {x}')
"""
This is a DOc string
Can do multiple lines
"""

## Map function helps to apply one 
# operation to all the elements of the list

def square(num):
    num1 = num **2
    return num1
# Same above function can be re-written as below
def square1(num): return num*2

x= square(5)
print(f'Square of 5 is {x}')

# If I need to apply the function(square) to all the
# elemenst in the list
# 1. Use loops
list1 = [5,3,4,8,2]
list2 =[]
for i in list1:
    list2.append(square(i))
print (list2)

# 2. Use Map function - in built function
list3 = list(map(square1,list2))
print (f'Pinting the list using Map function : {list3}')

# Lambda(Anonymous) functions
# Lambda expression for  "def square1(num): return num*2" is lambda num:num*2

list4 = list(map(lambda num:num*2,list1))
print (f'Printing list using lambda function : {list4}')

## Filter function could check for a condition in the list and Filter only the values we need from the list
# For ex: if I need to get only even number from the list , I could use Filter and Lambda function to filter only that

list1 =[2,67,45,22,34,45]
# we could use for loop and check the condition to do that
#2. Use Filter and Lambda function
# filter will return the elements only if it is true
list2 = list(filter(lambda x: x%2== 0, list1))
print (f'Even element list using Filter and Lambda fucntion is {list2}')



