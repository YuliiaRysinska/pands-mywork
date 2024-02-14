# get the program to generate a random number between 0 and 100 toguess
import random

while True:
    number1 = random.randint(0, 100)
    attempts = 0
    guess = int(input("Guess a random number between 0 and 100: "))
    attempts += 1

    if guess == number1:
        playAgain = input(
            f"correct! the secret number was indeed {number1}, and you guessed it in {attempts} attempts. play again? (yes/no) "
        )
        if playAgain == "yes":
            # generate a new number and make the user try again
            number1 = random.randint(0, 100)
            continue
        else:
            break
    elif guess > number1:
        print("Try a smaller number. ")
    else:
        print("Try a bigger number. ")
