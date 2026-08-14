# [expression for item in iterable]
#Modifying
#squares
nums = [1,2,3,4,5]
squares = [x*x for x in nums]
print(squares)

# double every number in a list

double = [x*2 for x in nums]
print(double)

# add ten 
print([x+10 for x in double])

# cubes
print([x**3 for x in nums])

# List Comprehension with Strings
# printing upper case
names = ["ali","Musadiq","David"]
print([x.upper() for x in names])
#Filtering
# Even numbers in seconds
# even = [x%2==0 for x in nums] wrong
even = [x for x in nums if x%2==0]
print(even)

#[expression for item in iterable if condition]

# Filtering Plus Modifying
#Squaring even numbers
squares = [x*x for x in nums if x%2==0]
print(squares) 

# condtional Statements
result = [
    "Even" if x % 2 == 0 else "Odd"
    for x in nums
]
marks = [35, 67, 82, 41, 90]
result = [
    "Pass" if mark >= 40 else "Fail"
    for mark in marks
]


# activity
numbers = [1,2,3,4,5,6]
numbers1 = [x*10 for x in numbers]
numbers2 = [x for x in numbers if x%2!=0]
numbers3 = [x*x for x in numbers2]

marks = [35, 72, 89, 41, 28, 95]
results =[ True if mark>=40 else False for mark in marks]

names = ["ali", "john", "musaddiq", "ahmed"]
namesCount = [len(x) for x in names]

print(numbers1,numbers2
      ,numbers3
      ,results
      ,namesCount
      )

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
mat = [x for row in matrix for x in row]

temperatures = [18, 25, 31, 16, 29, 35, 12]
F = [(C*9/5)+32 for C in temperatures if C>25 ]
print(mat,F)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums = [x*x*10 for x in numbers if x%2==0]