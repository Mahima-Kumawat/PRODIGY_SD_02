import random

def guessing_game():
    number_to_guess = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0
    
    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()