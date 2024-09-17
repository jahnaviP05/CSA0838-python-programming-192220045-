import random

def guess_number_game():
    number = random.randint(1, 100)
    attempts = 0
    while (guess := int(input("Guess the number: "))) != number:
        print("Higher!" if guess < number else "Lower!")
        attempts += 1
    print(f"Correct! You guessed it in {attempts + 1} attempts.")
guess_number_game()
