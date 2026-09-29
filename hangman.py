import random

# List of predefined words
words = ["python", "computer", "programming", "keyboard", "developer"]

# Select a random word
word = random.choice(words)

# Store correctly guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_attempts = 63
attempts = 0

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

# Main game loop
while attempts < max_attempts:

    # Display the word with blanks
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", attempts)
    print("Attempts remaining:", max_attempts - attempts)

    # Check if the player has guessed the complete word
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word!")
        print("The word was:", word)
        break

    # Ask the player for a letter
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check whether the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the letter to guessed letters
    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        print("Incorrect guess!")
        attempts += 1

else:
    print("\nGame Over!")
    print("The correct word was:", word)