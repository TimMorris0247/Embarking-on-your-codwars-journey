import random

secret_number = random.randint(1,10)

guess = int(input("Make a guess between 1-10:"))

if (secret_number == guess):
    print("Congratulations, you guessed the serect number!")
elif (guess < secret_number):
    print("Too Low!")
else:
    print("Too High!!")

