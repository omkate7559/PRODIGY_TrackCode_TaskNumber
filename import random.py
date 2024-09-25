import random

# Function to run the guessing game
def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0  # Track the number of attempts
    
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        # Prompt the user for a guess
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Compare the guess to the generated number
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                break  # Exit the loop if the guess is correct
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Run the guessing game
if __name__ == "__main__":
    guessing_game()
