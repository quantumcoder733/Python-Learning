def sum(num1 ,num2):
    return num1 + num2

def largest(num1 , num2 , num3):
    return max(num1,num2,num3)

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#Implementation of Fuunctions
print("Sum of 5 and 10 is:", sum(5, 10))
print("Largest among 5, 10 and 15 is:", largest(5, 10, 15))
print("Factorial of 5 is:", factorial(5))
print("Is 7 a prime number?", is_prime(7))
print("GCD of 48 and 18 is:", gcd(48, 18))  