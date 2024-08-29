
letter = input("Enter a letter: ")
if len(letter) == 1 and letter.isalpha():
    print(f"Unicode encoding for '{letter}' is: {ord(letter)}")
else:
    print("Invalid input. Please enter a single letter.")
