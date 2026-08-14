import numpy as np

a = np.array([1,2,3,4,5])
print(type(a))
print(a.ndim)
print(a.shape)
print(a.size)
print(a*5)
print(a**a)

b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(b)
print(b.shape)
print(b.size)
print(b.ndim)

#np.zeros(count,dtype)
c = np.zeros(5)
d = np.zeros((3,4))
print(c,d)

#np.ones(count,dtype)
e = np.ones((3,4))
print(e)

#np.full(shape,value)
f = np.full((2, 3), 9)
# [[9 9 9]
#  [9 9 9]]
print(f)

#np.arange(upl,ll,skip)
g = np.arange(1,11)
h = np.arange(2,21,2)
print(g)
print(h)
#np.linspace(start stop number)
i = np.linspace(1,10,5)
# Give me exactly 5 equally spaced values between 0 and 10
print(i)

# np.eye identity matrix
s = np.eye(5)
print(s)

# np.array()	Create array from existing data
# np.zeros()	Array of zeros
# np.ones()	    Array of ones
# np.full()	    Array filled with chosen value
# np.arange()	Values with fixed step
# np.linspace()	Fixed number of equally spaced values
# np.eye()	    Identity matrix
# np.random.rand()  	Random floats
# np.random.randint()	Random integers


#activity
zeros = np.zeros(10)
print(zeros)
ones = np.ones((3,4))
print(ones)
arr = np.arange(1,31,5)
print(arr)
lin = np.linspace(0,100,6)
print(lin)

rand = np.random.randint(0,50,(3,3))
print(rand)

arrr = np.arange(1,7).reshape((2,3))
print(arrr)