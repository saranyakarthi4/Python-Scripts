#inp = 'aabbcdeefffaabbcc'
# expected output ='a2b2c1d1e2f3a2b2c2'

def find_occur(inp):
    cnt = 1
    oup =''
    if len(inp) ==0:
        print (inp)
    elif len(inp) ==1:
        print (inp+'1')
    elif set(list(inp)) ==1:
        print (inp[0]+str(len(inp)))
    else:
        for i in range(0,len(inp)):
            if i == 0:
                oup = oup + inp[0]
            else:
                    if inp[i-1] != inp[i]:
                        oup = oup + str(cnt)  
                        cnt = 1
                        oup =oup +inp[i]
                    else:
                        cnt = cnt +1
        oup = oup + str(cnt)  
    return (oup)

print (find_occur('aabbcceeaaxxxxxxxxxxxxxxxxxxyyyyyyyyyyyyyyyyyyyyaaaaaaaaaaaaaaaa'))
print (find_occur(''))
print (find_occur('a'))
print (find_occur('1'))
print (find_occur('xx'))


