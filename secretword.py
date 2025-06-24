import random

secret_words = ["girlfriend", "boyfriend", "friend", "apple", "ghost"]
secret_word = random.choice(secret_words)
guesses = ""
guess_count = 0
guess_limit = 12
out_of_guesses = False

print("Guess the character: ")

while guess_limit > 0:
    failed = 0

    for char in secret_word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1
    
    if failed == 0:
        print(f"\nYou win The word was {secret_word}")
        break

    print()
    guess = input("Guess the character: ")

    guesses += guess
    if guess not in secret_word:
        guess_limit -= 1
        print("Wrong!")
        print("You have", + guess_limit, "more guesses")

        if guess_limit == 0:
            print("You lose")