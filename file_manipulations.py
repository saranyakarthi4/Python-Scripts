import os,csv
import copy

#Reading csv file
# each row in csv will be return in a list and lt and concating all teh list and making as one big list
lt =[]
f = csv.reader(open("/Users/skarthi/Documents/test_data.csv","rb"),delimiter=",")
for i in f:
	print(', '.join(i))
	print(type(i))
	print (i)
	lt = lt+i
print ("reading from csv file",lt)
print ("count of space is",lt.count(" "))

print ("Reading from a txt file::")
file = open("/Users/skarthi/Documents/python_text.txt","r+")
print ("Displaying all contents of a file")
print (file.read())

print ("reading usig loop functions")
file2 = open("/Users/skarthi/Documents/python_text.txt","r+")
cnt = 0
line_cnt = 0
temp_list =[]
full_list =[]
for line in file2:
	print (line)
	temp_list = line.split(" ")
	full_list = full_list +temp_list
	cnt = cnt + len(temp_list)
	print (cnt)
	line_cnt = line_cnt + 1
print ("total number of words in the list is {}".format(cnt))
print ("Number of lines in the text file is {}".format(line_cnt))


# full list contains all the words in the text file
print ("Words starting with -T- in the file")
t_words = ""
for i in full_list:
	if i[0]=='T':
		t_words = i +" ," + t_words
print (t_words.replace(t_words[-1],""))	


##most occuring word in the file
print ("Most occuring word in the file is {}",max(full_list,key=full_list.count))
copied_list = copy.copy(full_list)
def length_str(a):
	return len(a)
copied_list.sort(key = length_str)
print ("Lengthest word in the file is {}",copied_list[-1])

#print ("displaying the contents of a text file by new-line seperator",file.readlines())
#file.seek(0)
#print ("Displaying 2nd line from the file",file.readline(2))
#file.close()

##Writing into csv file
#f = csv.writer(open("/Users/skarthi/Documents/test_2.csv","wb")
#i.writerows("This is the first line")
