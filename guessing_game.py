import random

def guessing_game()->None:
    low = int(input("What is the lowest range you want to guess: "))
    high = int(input("What is the highest range you want to guess: "))

    print(f"You have 7 tries to guess the number between {low} and {high}")

    number = random.randint(low, high)
    max_tries = 7
    tries = 0

    while tries <= max_tries:
        tries += 1
        num = int(input("Guess the number: "))
    
        if num == number:
            print(f"Congratulations! You guessed {number} in {tries} tries")
            break
        elif num < low or num > high:
            print("Not in range")
        elif num < number:
            print("Wrong guess! You guessed too low!")
        elif num > number:
            print("Wrong guess! You guessed too high!")
        elif tries >= max_tries and num != number:
            print(f"You lose! The number was {number}")
            break

guessing_game()