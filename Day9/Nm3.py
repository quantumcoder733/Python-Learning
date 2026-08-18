#Mathematical and Statistical Operations
import numpy as np

a = np.array([10,20,30,40,50])
print(a.sum)
#or
print(np.sum(a))
# Mean = average
print(np.mean(a))
print(np.min(a))
print(np.max(a))
print(np.median(a))
print(np.std(a))
print(np.argmin(a))
print(np.argmax(a))
# np.sum(a)
# np.mean(a)
# np.median(a)
# np.min(a)
# np.max(a)
# np.std(a)
# np.var(a)
# np.argmin(a)
# np.argmax(a)
#This give the sum row wise
# example consider
b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(np.sum(b,axis = 0))
print(np.sum(b,axis = 1))

# np.sum(a, axis=0)
# np.sum(a, axis=1)

# np.mean(a, axis=0)
# np.mean(a, axis=1)

#Activity
c = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(np.sum(c))
print(np.mean(c))
print(np.min(c))
print(np.max(c))
print(np.argmin(c))
print(np.argmax(c))
print(np.sum(c,axis = 0))
print(np.sum(c,axis = 1))
print(np.mean(c,axis = 0))
print(np.mean(c,axis = 1))


#Numpy Arithmatic and Universal Functions
arr = np.array([1, 4, 9, 16, 25])
print(np.sqrt(arr))
print(np.exp(arr))
print(np.log(arr))

brr = np.array([-10, -5, 0, 5, 10])

print(np.abs(brr))
# [10  5  0  5 10]

crr = np.array([1.234, 5.678, 9.876])

print(np.round(crr, 2))
# [1.23 5.68 9.88]

#Activity
an = np.array([-4, -1, 0, 1, 4, 9, 16])
print(np.abs(an))
print(np.sqrt(an))
print(np.multiply(an, an))
print(np.exp(an))
print(np.log(an))
ann = np.array([1.2345,2.345,4.5678,1.6543])
print(np.round(ann, 2))

print(an.sort)
print(np.sort(ann, axis = 0))
print(np.sort(ann, axis = 1))
print(np.sort(ann))
print(np.argsort(ann, axis = 0))
print(np.argsort(ann, axis = 1))
print(np.argsort(ann))

print(np.where(ann>25))
a = np.array([10, 20, 30, 40, 50])

result = np.where(a > 25, 999, a)

print(result)
# [ 10  20 999 999 999]

a = np.array([1, 2, 2, 3, 3, 3, 4, 4])

print(np.unique(a))
# [1 2 3 4]

values, counts = np.unique(a, return_counts=True)

print(values)
print(counts)
# [1 2 3 4]
# [1 2 3 2]
# Matrix Multiplication
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(a @ b)

#Activity
a = np.array([50, 20, 40, 10, 30, 20, 50])
print(np.sort(a))
print(np.argsort(a))
print(np.where(a > 25))
print(np.where(a>30,999,a))
values, count = (np.unique(a,return_counts=True))
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])
print(a*b)
print(a@b)