#All Basics On 15/07/2026
intvar = 10
print(intvar)
charvar = 'A'
print(charvar)
boolvar = True
print(boolvar)
nonevar = None
print(nonevar)

score = 70
#if elif else statement 
if score>=90:
    print("A")
elif score>=80:
    print("B")
else:
    print("C")

#four built-in data structures in python
#1 List(ordered,Mutable,Allows Duplicates)
listvar = ["Alice", "Bob", "Charlie"]
print(listvar)
listvar.append("David")
print(listvar)
listvar.remove("Bob")
print(listvar)

#2 Dictionaries(Key-Value Pair, Unordered, Mutable, No Duplicates)
dictvar = {"Name": "Alice", "Age": 25, "City": "New York"}
print(dictvar)
dictvar["Age"] = 26
print(dictvar)
dictvar["email"] = "alice@example.com"
print(dictvar)

#3 Tuples(Ordered, Immutable, Allows Duplicates)
tuplevar = ("Alice", "Bob", "Charlie")
print(tuplevar)
tuplevar = tuplevar + ("David",)
print(tuplevar)
tuplevar = tuplevar[:2] + ("Eve",) + tuplevar[2:]
print(tuplevar)

#4 Sets(Unordered, Mutable, No Duplicates)
setvar = {"Alice", "Bob", "Charlie"}
print(setvar)
setvar.add("David")
print(setvar)
setvar.remove("Bob")
print(setvar)

#Functions
def add_numbers(a, b):
    return a + b

a = 5
b= 10
c = add_numbers(a, b)
print("The sum of a=", a, "and b=", b, "is:", c)

for i in setvar:
    print(i)
for i in range(5):
    print(i)
while a < 10:
    print(a)
    a += 1
