# Chat-GPT-3 code
import random

# Generate a random number between 1 and 100
answer = random.randint(1, 100)

# Start the guessing game
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

# Print a hint
print(f"It is close to the number {answer - (random.randrange(1, 10))}")

while True:
    # Get the user's guess
    guess = int(input("Your guess: "))

    if guess == answer:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess > answer:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")
