#printing 1 to 100
for i in range(1,101):
    print(i)
print("\n")


#even numbers from 1 to 100
for i in range(1,101):
    if i%2==0:
        print(i)
print("\n")


#table of a number
a = int(input("Enter the Number which u want to print table of :"))
for i in range(1,11):
    print(f"{a} x {i} = {a*i}")

