#function
def Numbers():
    return [1,2,3,4,5]

#Generators
def Nums():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

a = Numbers()
print(a)
b = Nums()

print(next(b))
for i in b:
    print(i)


#Stop Iteration
# print(next(b))

# Generator With Loop
def Loop():
    for i in range(1,21):
        yield i

for i in Loop():
    if i % 2 == 0:
        print(i,end=" ")


#Gen vs List Comprehension
# [ ... ]   → List → all values stored
# ( ... )   → Generator → values produced when needed