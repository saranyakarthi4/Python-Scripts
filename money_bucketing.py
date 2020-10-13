valid_currency = [1,2,5,10,20,50,100,500,1000]
money =  958
m= money


i = 1
m_list =[]
while (money):
    x= money%10
    money = int(money/10)
    m_list.append(x*i)
    i= i*10
m_list =sorted(m_list,reverse=True)
print ('m_list is ',m_list)
o_list =[]
n=len(m_list)
def find_pair(m):
    vc = sorted(list(filter(lambda x: x<=m, valid_currency )),reverse=True)
    print ('vc is ',vc)
    if m in vc:
        o_list.append((str(m) +'-'+ str(1)))
    else:
        if len(vc) >= 1:
            o_list.append(str(max(vc))+'-'+str(int(m / max(vc))))
            m1 = m % max(vc)
            find_pair(m1)
    return (o_list)


for i in range(0,n):
    l= find_pair(m_list[i])
print ('value is ' ,l)



