# modify the program (guess1.py) above, so that the program tells the user if there guess is too high or too low,
# each time they guess. HINT: put an if statement inside the while loop

numberToGuess = 30
guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else:
        print("too high")
    guess = int(input("Please guess again:"))
print("Well done! Yes the number was ", numberToGuess)
