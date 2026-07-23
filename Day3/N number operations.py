number = int(input("Enter the Number : "))
sum = 0
for i in range (1,number+1):
    sum = sum +i    
print(sum)

#factorial
a = int(input("Enter the Number : "))
factorial = 1
for i in range(1,a+1):
    factorial = factorial * i
print(f"The factorial of {a} is {factorial}")

#reverse of a number
b = int(input("Enter the Number : "))
rev = 0
while(b>0):
    dig = b % 10
    rev = rev * 10 + dig
    b = b // 10
print(f"The reverse of the number is {rev}")
#palindrome
if b==rev:
    print("The number is a palindrome")
