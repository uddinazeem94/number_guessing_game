from random import randint
from replit import clear
from time import sleep


def num_guess_game():
    clear()
    # Number guessing game
    guess_count = 0
    # setting total guesses as 0
    total_guesses = 0
    # printing a welcome message
    print("Welcome to the number guessing game!")
    #time.sleep(1)

    # Setting difficulty
    difficulty = input("Choose your difficulty level: Type 'easy' or 'hard'\n").lower()
    if difficulty == 'easy':
        total_guesses = 10
    elif difficulty == 'hard':
        total_guesses = 5
    print("I'm thinking of a number between 1 and 100...")
    #time.sleep(1)

    # Taking a random number to guess
    number = randint(1, 101)
    
    
    # Looping till guess count reaches total guesses
    while guess_count <= total_guesses:
        print(f"You Have {total_guesses-guess_count} guesses remaining..")
        message1 = "Make a guess>> "
        guess = int(input(message1))
        if guess == number:
            print("YOU GUESSED IT!!!! Congrats")
            break
        elif guess < number:
            if number - guess > 10:
                print("Too Low!!")
            elif number - guess < 10:
                print("A bit low!")
            guess_count += 1
        elif guess > number:
            if guess - number > 10:
                print("Too High!!")
            elif guess - number < 10:
                print("A bit High!")
            guess_count += 1
        # End of guesses check condition
        if guess_count == total_guesses:
            print(f"You Lose!! The number was {number}")
            break
    while True:
        run_again = input("Do you wish to play again? type 'y' or 'n'... ")
        if run_again == 'y':
            num_guess_game()
        elif run_again == 'n':
            exit()
        else:
            print("Invalid input...")

num_guess_game()