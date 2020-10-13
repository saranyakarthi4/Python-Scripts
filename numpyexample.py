import numpy as np

# create array of 10 zeros/10 ones
arr1 = np.ones(10)
print (arr1)

# create array of 10 5s
arr1= np.ones(10) * 5
print (arr1)

arr1 = np.arange(10,51,1)
print (arr1)

arr1 = np.arange(10,51,2)
print (arr1)

#create 3X 3 matrix from 0 to 8
arr1 = np.arange(9).reshape(3,3)
print (arr1)

# create identify matrix
arr1 = np.eye(3)
print (arr1)

# get random number between 0 and 1
arr1 = np.random.rand(1)
print (arr1)

# get random 25 numbers from normal distribution
arr1 = np.random.randn(25)
print (arr1)


arr1 =  np.arange(0.01,1.01,0.01).reshape(10,10)
print (arr1)
print (np.linspace(0,10,20))

arr1 = np.arange(1,26).reshape(5,5)
print (arr1)
print (arr1[2:,1:])
print (arr1[3][4])
print (arr1[:3, 1:2])
print (arr1[4])
print (arr1[3:,:])
print (np.sum(arr1))
print (np.std(arr1))
print (arr1.sum())
print ("Sum of all columns in matrix, axis = 0,")
print ("Sum of all rows in matrix, axis = 1,")
print (arr1.sum(axis= 0))