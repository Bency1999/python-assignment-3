import random

secret_number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess between 1 and 10.")
        continue
    elif guess > secret_number:
        print("Too high! Try again.")
        attempts -= 1
    elif guess < secret_number:
        print("Too low. Try again.")
        attempts -= 1
    else:
        print("Congratulations! You guessed the correct number!")
        break
else:
    print("Better luck next time!")