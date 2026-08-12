


try:
    a = int(input("Enter the First Number : "))
    b = int(input("Enter the Second Number :"))
    a/b
except ZeroDivisionError:
    print("Cannot be divided By Zero")
except ValueError:
    print("Invalid Input !!")

else:
    print(f"{a}/{b} = ",a/b)
