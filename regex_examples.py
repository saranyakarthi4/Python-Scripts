import re
# multiline text string
str1 ="""djfkdjf
gjkdjgd
dfkdfj"""
print (str1)

# finding phone number in the string
str1 = "jfhjs 6782345678 dhfdhf 67vdh fkdjfk 89 "
ph_no= (re.findall(r'\d{10}',str1))
print (ph_no)


# finding a string within string eg: sd in "ersddkjfksdkdfksd"
if re.search("sd","sdfrfrsdfrfsd"):
	print ("Match Found")
else:
	print ("Match Not Found")

# check whether is a phone number 
ph1 = "98-890-6789"
if re.search(r'\d{3}-\d{3}-\d{4}',ph1):
	print ("yes, phone number")

else:
	print ("not a phone number")

# Getting phone number from text
str1 ="ksdfjks (408) 678-7891 dksfksk"
ph_nos = re.findall(r'\(\d{3}\) \d{3}-\d{4}',str1)
print ("phone numbers:",ph_nos)
for i in ph_nos:
	print ("printing phone_number from the text",i)

# finding number of occurence of sd in the string
str2  = """ I am a good woman and I like food and I work every day and I love my kids and
I love my family"""
count = re.findall("I",str2)
print ("I letter cames {} times.".format(len(count)))

# displaying till special charater
txt = re.findall(r'(^\w+)',"saranya, is my name")
print ("displaying till special character", txt)

# replace word in the string
s= re.sub(("min"),"max","minimumminhdshmin")
print ("Replaced string ",s)

# finding words starting with Q
count = 0
list1 =["guy","gale","uruselenum"]
print ("elements startng with g")
match_list=[]
for i in list1:
	if re.findall(r'[g]+',i):
		match_list.append(i)
print ("Names starting with g",match_list)

# validating emial and password
str1 = 'purple alice-09@google.com, blah monkey bob_1@abc.com blah dishwasher'
emails = re.findall(r'[w._]+@[w.-]+',str1)
for i in emails:
	print ("emails",i)
######not working#######

# get all the text before "end" in "dsj is the end"
str1 = "This is the end"
str2 = re.findall(r'[^end]',str1)
print ("Printing all the text before END",str2)


# get all text after "yu" in "hksjdks yu odd ui"
str1 = "I am a good girl"
str2 = re.findall(r'good+$',str1)
print ("printing all the text after good: ",str2)


#finding duplicate charhters in a sentence


# find max numeric value from a sentence "I got 100 but I need 1000 and if I get 100000 I will be more happy"
str1= "I got 100 but I need 1000 and if I get 100000 I will be more happy"
p1 =re.compile(r'\d+')
print ("Maximum number in the string ",max((p1.findall(str1))))
li =[]
li= re.findall(r'[\d]+',str1)
print ("printing numbers list ",li)

# finding positions of the number
it = p1.finditer("I got 100 but I need 1000 and if I get 100000 I will be more happy")
print ("printing iteration list",it)
for i in it:
	print ("displaying position of each string",i.span())

# finding position of a particular string

str1 = "we need to inform him the information"
for i in re.finditer("inform",str1):
	tuple1 = i.span()
	print ("Displaying the indexes of inform word in the string",tuple1)

# remove duplicate words in a string " I am a geek,brillant and good geek"

# print common letter in both strings /sentence

