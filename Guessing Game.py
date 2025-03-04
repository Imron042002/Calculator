import random

def get_guess():
    while True:
        try:
            return int(input("Enter your guess (1-100): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Guessing Game! Try to guess the number between 1 and 100.")

    while True:
        guess = get_guess()
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please guess a number within the range of 1 to 100.")
            continue

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

if __name__ == "__main__":
    guessing_game()