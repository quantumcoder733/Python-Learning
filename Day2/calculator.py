a = int(input("Enter the First Number :"))
b = int(input("Enter the Second Number :"))
o = input("Enter the Operation (+, -, *, /): ")

if(o=="+"):
    print(f"the sum of {a} and {b} is {a+b}")
elif(o=="-"):
    print(f"the difference of {a} and {b} is {a-b}")
elif(o=="*"):
    print(f"the product of {a} and {b} is {a*b}")
elif(o=="/"):
    if(b==0):
        print("Division by zero is not allowed.")
    else:
        print(f"the division of {a} and {b} is {a/b}")
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")