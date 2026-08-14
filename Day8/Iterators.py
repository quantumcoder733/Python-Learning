#Iterators

numbers = [10, 20, 30, 40]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

class Count:
    def __init__(self, max):
        self.current = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

numbers = Count(5)

for x in numbers:
    print(x)