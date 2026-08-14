#Slicing
import numpy as np
a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

#print:
# 50
print(a[1,1])
# 70
print(a[2,0])
# Entire first row
print(a[0])
# Entire third column
print(a[:,2])
# [20, 30]
print(a[0,1:3])
# [40, 50, 60]
print(a[1])


#Challenge 2
a = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])

# All values greater than 30
print(a[a>30])
# All values less than 25
print(a[a<25])
# All even numbers
print(a[a%2==0])
# All values between 20 and 40 inclusive
print(a[20,41])
# Replace every value greater than 30 with 999
arr = a[a>30] =999
print(arr)

# challenge 3

a = np.arange(1, 25)
print(a.reshape((4,6)))
print(a.reshape((6,4)))
print(a.reshape((3,8)))
print(a.reshape((2,12)))
print(a.reshape((4,-1)))