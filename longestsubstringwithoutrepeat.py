ip1 ='dvdf'
# output is 3 as 'vdf'
o_list =[]
val =''
for i in range(len(ip1)):
    print ('entering the I loop')
    flag =0
    val =''
    for j in range(0,len(ip1)):
        print ('entering J loop')
        print ('check is ',ip1[j])
        if ip1[j] not in val:
            val = val + ip1[i]+ip1[j]
            print ('val is ',val)
        else :
            flag = 1
        if flag ==0:
            o_list.append(val)
            print ('o_list is',o_list)
