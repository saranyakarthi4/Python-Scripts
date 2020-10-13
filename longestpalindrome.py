str1 = 'abcda'
if str1=='':
    print ('')
elif len(str1) ==1:
    print (str1)
elif len(set(str1)) == 1:
    print (str1[0])
else:
    p_len = 0
    palin_op =''
    for i in range(0,len(str1)):
        for j in range(i+1, len(str1)):
            #print (i,j,str1[i],str1[j])
            if str1[i] == str1[j]:
                x = str1[i:j+1]
                #print (x)
                if x== x[::-1]:
                    if p_len < len(x):
                        p_len =len(x)
                        palin_op = x
    if palin_op =='':
        print (str1[0])
    else:
        print (palin_op)