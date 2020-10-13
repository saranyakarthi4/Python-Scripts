# Find the pair of alphabets in a alphanumeric string whose sum of numbers inbetween is always 9
# Input: a54b12c
# Output:
# a,b

# Input: a55b234cd9f63de54x3m

# Output:
# b,c
# b,d
# d,f
# f,d
# f,e
# e,x
def finding_pair(str1):
    if len(str1)<= 2:
        print ('')
    else:
        t_list =[]
        l=[]
        s=0
        for i in range(0,len(str1)):
            if str1[i].isalpha():
                l.append(i)
                l.append(str1[i])
                t_list.append(l)
            l=[]
        for i in range(0,len(t_list)-1):
            if int(t_list[i][0])+1 == int(t_list[i+1][0]):
                x= (str1[int(t_list[i-1][0])+1:int(t_list[i+1][0])])[:-1]
            else:    
                x= (str1[int(t_list[i][0])+1:int(t_list[i+1][0])])
            if x=='' or x is None:
                x=0
            else:
                x= int(x)
                while (x):
                    s= s+x%10
                    x=int(x/10)
                if int(s)==9:
                    if int(t_list[i][0])+1 == int(t_list[i+1][0]):
                        print (t_list[i-1][1],t_list[i+1][1] )
                    else:
                        print (t_list[i][1],t_list[i+1][1] )
            s=0
    return ''

print ('output as below')
print (finding_pair(''))
print (finding_pair('a2'))
print (finding_pair('ab'))
print (finding_pair('a54b12c'))
print (finding_pair('a55b234cd9f63de54x3m'))
print (finding_pair('a9b34c91d'))
