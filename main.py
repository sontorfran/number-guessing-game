import random

n = random.randrange(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < n:
        print("Your guess is too low")
    elif guess > n and guess <= 100:
        print("Your guess is too high")
    elif guess > 100:
        print("Your guess is out of range. Please guess a number between 1 and 100.")
    else:
        print("Congratulations! You guessed the random number!")
        break
