input_list =['A,B,C,D','B,E,F','D,G,I','G,H']
# A is the manager of B,C,D
# B is the manager of E,F
# D is the manager of G,I etc
#We need to print in the mgr and their reportee in the below format
'''
A
....B
........E
........F
....C
....D
........G
............H
........I
'''

unnest_list =[]
unique_list =[]
mgr_dict ={}
# unnesting the list
for i in input_list:
    ele =list(i.split(','))
    unnest_list.extend(list(i.split(',')))
    mgr_dict[ele[0]] = ele[1:]
for i in unnest_list:
    if i not in unique_list:
        unique_list.append(i)

print ('unnest list : ',unnest_list)
print ('unique list :',unique_list)
print ('mgr dictionary : ',mgr_dict)
# Creating the dictionary with mgr as key and its employess as values
o_list =[]
for i in unique_list:
    if i not in o_list:
        if i =='A':
            o_list.append(i)
        else :
            if i in mgr_dict.keys():
                o_list.append(i)
                for k,v in mgr_dict.items():
                    if i==k:
                        o_list.extend(v)
            else:
                o_list.append(i)

print ('o_lost ',o_list)
output_dict = dict.fromkeys(o_list,0)
print ('output_dict : ',output_dict)
n=len(unique_list)
for i in o_list:
    if i in mgr_dict.keys() and unnest_list.count(i)==1:
        output_dict[i]= 0  # root node
    else:
        for k,v in mgr_dict.items():
            if i in v:
                mgr_depth = output_dict[k]
                output_dict[i] = mgr_depth +1

print ('dictionary with depth : ',output_dict)
for i,j in output_dict.items():
    if j==0:
        print (i)
    else:
        for x in range(j):
            print ('....',end='')
        print (i)


