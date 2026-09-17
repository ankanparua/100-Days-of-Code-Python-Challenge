import art
import random
is_game_over = False
MAX_LIVES = 0


def choose_difficulty():
    choose = input("Choose a difficulty. Type 'easy' or 'hard': ")
    global MAX_LIVES
    global is_game_over
    if choose == "easy":
        MAX_LIVES = 10
    elif choose == "hard":
        MAX_LIVES = 5
    else:
        is_game_over = True
    return

def check_guess(guess, number):
    global is_game_over
    global MAX_LIVES
    if guess == number:
        is_game_over = True
        print(f"You got it! The answer was {number}.")
    elif guess < number:
        print("Too low.\nGuess again.")
    else:
        print("Too high.\nGuess again.")


def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    global MAX_LIVES
    global is_game_over
    choose_difficulty()
    number = random.randint(1, 100)

    while not is_game_over:
        if MAX_LIVES <= 0:
            print("You've run out of guesses. Run again to Play Again.")
            is_game_over = True
            break
        print(f"You have {MAX_LIVES} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        check_guess(guess, number)
        if is_game_over == False:
            if MAX_LIVES > 0:
                MAX_LIVES -= 1




play_game()

