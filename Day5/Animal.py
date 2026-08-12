#polymorphism

class Animal:
    def make_sound(self):
        print("Animal Sound")

class Dog:
    def make_sound(self):
        print("Barks")

class Cat:
    def make_sound(self):
        print("Meows")

animals = [Dog(),Cat()]

for animal in animals:
    animal.make_sound()
