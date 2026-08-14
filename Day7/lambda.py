# Normal function
def add1(a,b):
    return a+b

# Lambda
add2 = lambda a,b:a+b

print(add1(12,12),add2(12,12))

# lambda arguments : expression
square = lambda x:x*x
print(square(5))

#map-> Applies a function to every element in a list
nums = [1,2,3,4,5]
result = list(map(lambda x:x*2,nums))
print(result)

#filter-> Filters elements based on a condition
result = list(filter(lambda x:x%2==0,nums))
print(result)

# square even numbers
evens = list(filter(lambda x:x%2==0,nums))
squared = list(map(lambda x:x*x ,evens))
print(squared)

# 1 fline for both 
squared = list(map(lambda x:x*x ,(list(filter(lambda x:x%2==0,nums)))))
print(squared)

