# Simple Python programs for Beginners
# different ways of printing
age = 33
name = "skarthi"
print ("my name is {} and my age is {}".format(name,age))
# we can do as follows
print ("my name is {n} and my age is {a} and again my name is {n}".format(n=name,a=age))

# python slicing
s= "abcdefghijklmnop"
print (s[2:-1])

# lists appending
lista =["a","b","c"]
lista.append("d")
print (lista)


nested_list1 = [1,2,[3,4,["target"]]]
# to retrive "[target]" list from the above nested list
print (nested_list1[2][2])
# to retrive only the word target  from the above nested list
print (nested_list1[2][2][0])

# Dictionaries
d1 ={"key1": "value1","key2": 123}
print (d1, d1["key1"])

d= {"key1":{"values": [1,2,3]}}
# to retrive 2 from the above dictionary
print (d["key1"]["values"][1])

# printing dictionaries keys, values and both
rows =(1,2,3)
cols =0
dict1 = dict.fromkeys(rows,cols)
print (dict1)
print (dict1.keys(), dict1.values(),dict1.items())


# Tuples (they are immutable which means we cannot change the vlaues inside them like list)
list_1 =[1,2,3]
list_1[0] = 5
print(list_1)

tuple_1 =(1,2,3)
#tuple_1[0]= 5    throws an error saying "'tuple' object does not support item assignment"
print (tuple_1)
# tuple unpacking
tuple1 = [(1,2),(3,4),(5,6)]
print (tuple1)
for a,b in tuple1:
    print (a)
    print (b)


# Sets is the collection of unique elements in the list
list_1 = [1,1,1,2,2,2,3,3,3,4,4,4,5,5]
print(set(list_1))
s= set(list_1)
s.add(6)
print (s)
s.add(6)
print (s)

#Conditional statements
if 1== 1:
    print ("true")
else:
    print ("false")


# Loops
x =[1,2,3,4]
x1=[]
for i in x:
    if i <5 :
        x1.append(i)
print (x1)
x2_list =[i*i for i in x]
print (x2_list)

for i in range(5):
    print (i)
print ("bye!")

################
print (list(range(3,15,2)))
################


# Functions
def print_my_name(str="Default name"):
    print (str)

#print_my_name("Saranya")   
print_my_name()

def square_fn(num = 1):
    return (num*num)

out = square_fn(5)
if out == 25:
    print (out)
else:
    print (5)
print ("Bye!")


print ("x" in [1,2,3])

### Strings
str1 = "This is my name"
list1 =(str1.split())
print (str1.split())
print (list1)


# MAP FUNCTION  used for applying a function to all the elements in a list

#Exercise 1:
print (7**4)

str1 ="Hi! this is Saranya"
print (str1.split())

planet ='Earth'
diameter = 76789
print ("The diameter of {p} is {d}".format(p=planet,d=diameter))

lst =[1,2,[3,4], [5,[100,200,["hello"]],23,22]  ,1,7]
print ((lst[3][1][2][0]))

d1= {"k1":[1,2,3,{"tricky":["oh","man","inception",{"target":[1,2,3,"hello"]}]}]}
print (d1)
print (d1["k1"][3]["tricky"][3]["target"][3])

def get_domain(eid= "xyx@domain.com"):
    return (eid.split("@")[1])

str1 ="skarthi@gmail.com"
out_str = get_domain(str1)
print (out_str)

def find_dog(str = "dog"):
    if "dog" in str.split():
        return True
    else:
        return False

input_str ="WHere is the dog as I like your dog ?"
output_ans = find_dog(input_str)
print (output_ans)

def count_dog(input_str):
    c=0
    for i in input_str.split():
        if i== "dog":
            c = c+1
    return c

cnt_dog = count_dog(input_str)
print ("no of times dog occur in the sentence is {}".format(cnt_dog))

# Map function in Python
def square_fn(var):
    return var*var

list1 =[1,2,3,4,5]
print (list(map(square_fn,list1)))

# lambda function
print (list(map(lambda var: var*var, list1)))

# filter function will return only the values in the list that satisfies the condition
print (list(filter(lambda var:var%2==0, list1)))

str1 ="My Name is Saranya"

seq  = ['soup','dog','salad','cat','great']
print (list(filter(lambda str1 : str1[0].lower()=='s', seq)))

# IF Birthday, then speed is 65 is no tickets, 66 -> 85 , small ticket, else big ticket
# IF not Birthday, then speed is 60 is no tickets, 61 -> 80 , small ticket, else big ticket

def get_result(speed, bday):
    if bday =='Yes':
        if speed <= 65:
            ticket_status = "No Ticket"
        elif speed >= 66 and speed <= 85:
            ticket_status = "small Ticket"
        else:
            ticket_status = "Big Ticket"
    else:
        if speed <= 60:
            ticket_status = "No Ticket"
        elif speed >= 61 and speed <= 80:
            ticket_status = "small Ticket"
        else:
            ticket_status = "Big Ticket"
    return ticket_status

input1 = get_result(80,'No')
print (input1)



