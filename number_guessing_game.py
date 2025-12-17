import shlex
import sys
from enum import Enum
import random

class GameLevel(Enum):
    Easy = 1
    Medium = 2
    Hard = 3

class LevelChances(Enum):
    Easy = 10
    Medium = 5
    Hard = 3

user_level_input = input(
    "Welcome to the Number Guessing Game! \n"
    "I'm thinking of a number between 1 and 100. \n"
    "You have several chances to guess the correct number based on the difficulty level. \n\n "
    "Please select the difficulty level: \n"
    "1. Easy (10 chances) \n"
    "2. Medium (5chances) \n"
    "3. Hard (3 chances) \n\n"
    "Enter your choice: ")

user_level = shlex.split(user_level_input)
game_level = int(user_level[0])
try:
    level = GameLevel(game_level)
except ValueError:
    print('ERROR: Difficulty level is not supported')
    sys.exit(1)

print(f"Great! You have selected the {GameLevel(game_level).name} difficulty level. "
                       f"Let's start the game!\n")

game_round = 0
attempts = 0
while True:
    game_round += 1
    attempts = 1
    actual_number = random.randint(1, 100)
    level_chance = GameLevel(game_level).name
    chances = LevelChances[level_chance].value

    while True:
        if attempts > chances:
            another_round_input = input("You have exceeded the chances to guess, would you like another round?\n "
                  "Enter y or n: ")
            another_round = shlex.split(another_round_input)[0]
            if another_round == 'y':
                break
            elif another_round == 'n':
                sys.exit(0)

        if attempts == chances:
            print('This is your last chance')

        user_guess_input = input(f"Enter your guess: ")
        try:
            user_guess = int(shlex.split(user_guess_input)[0])
        except ValueError:
            print("Please enter a valid number.")
            continue
        if user_guess > actual_number:
            print(f'Incorrect! The number is less than {user_guess}.')
            attempts += 1


        elif user_guess < actual_number:
            print(f'Incorrect! The number is greater than {user_guess}.')
            attempts += 1


        elif user_guess == actual_number:
            print(f'Congratulations! You won in round {game_round} '
                  f'with {attempts} attempt(s).')
            sys.exit(0)


