list1 = [20, 31, 5, 1, 591, 1351, 693]

for x in range(len(list1)- 1):
    for i in range(len(list1)):
        if list1[i] > list1[i+1]:
            t= list1[i+1]
            list1[i+1] = list1[i]
            list1[i] = t
        print (list1)
print (list1)

from datetime import datetime
account =[['Date','Credit','Debit','Balance']]

def transaction():
    now = datetime.now()
    dayMonthYear = str(now.day)+'/'+str(now.month)+'/'+str(now.year)
    validInput = False
    while validInput == False:
        creditQ = input('Do you want to credit your account in this transaction? Y/N').lower()
        if creditQ == 'y':
            validInput = True
            credit = float(input('How much do you want to credit your account? '))



transaction()
