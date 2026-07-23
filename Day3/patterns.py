for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print("\n")


for i in range(1,6):
    for j in range(1,i+1):
        print(f"{i}",end="")
    print("\n")

for i in range(1,6):
    for j in range(1,i+1):
        print(f"{j}",end="")
    print("\n")

for i in range(1,6):
    for j in range(i,0,-1):
        print(f"{j}",end="")
    print("\n")

i = 5
while i>=1:
    j = 1
    while j<=i:
        print("*",end="")
        j = j + 1
    print("\n")
    i = i - 1