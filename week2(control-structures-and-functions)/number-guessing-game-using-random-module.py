import random
def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                return
            print(f"Attempts left: {max_attempts - attempts}")
        except ValueError:
            print("Please enter a valid number.")
    print(f"Sorry, you've run out of attempts. The number was {secret_number}.")
    return
def main():
    number_guessing_game()
    while True:
        play_again = input("Would you like to play again? (yes/no): ")
        if play_again == "yes" or play_again=='YES':
            number_guessing_game()
        else:
            break
main()