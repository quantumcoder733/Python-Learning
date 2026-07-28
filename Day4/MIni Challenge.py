import random as rd
num = rd.randint(1,100)

while True:
    guess = int(input("Guess a NUmber Between 1 to 100 :"))
    if guess == num:
        print("Congratulations! You guessed the number.")
        break
    elif guess < num:
        print("Try a higher number.")
    else:
        print("Try a lower number.")