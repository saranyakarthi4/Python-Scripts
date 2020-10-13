import datetime
#import numpy
from datetime import timedelta
#from dateutil.relativedelta import relativedelta

#from dateutil.relativedelta import relativedelta

print (datetime.datetime.now())
print ("Printing day of today",datetime.datetime.now().strftime("%A"))


# From the date "2018 -09-13"  print the first working day of the week (monday)
# https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
x= datetime.datetime(2011, 9, 10)
days_diff = int(x.strftime("%w"))
print ('days_diff is {}'.format(days_diff))
print (datetime.datetime(2018, 9, 13) - timedelta(days = days_diff-1))

# for a date, print 1st and last date of the month
day_no = int(x.strftime("%d"))
print (day_no)
month_no = int(x.strftime("%m"))
print ("Print 1st day of month : ",(x - timedelta(days = (day_no-1))).strftime("%Y-%m-%d")  )
print ("print last day of month : ",((datetime.datetime(x.year,(x.month+1),1)) - timedelta(days = 1)).strftime("%Y-%m-%d"))

# for the given date range, give the number of working days
start_date = datetime.datetime(2018,9,1)
end_date = datetime.datetime(2018, 9,10)
count = 0
while (start_date<=end_date):
	if (int(start_date.strftime("%w")) != 0 and int(start_date.strftime("%w")) != 6):
		count = count+ 1
	start_date = start_date + timedelta(days = 1)
print ("No of working days ",count)

# find the date for 2015W15
str1= '2015W15'
print (str1[:4])
print (str1[-2:])
print (str1[2:3])

print ("Date of 2015W15 is {}".format(datetime.datetime(int(str1[:4]),1,1) + timedelta(days = ((int(str1[-2:]) * 7) -1)                )))
