import random
# Number guessing game:
lowest_num = 0
highes_num = int(input("Lowest number is 0 (by default), Enter highest number: "))
computer_guess = random.randint(lowest_num, highes_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highes_num}")
need_help = input(print("Understand the game first?(y/n): "))
if need_help == "y":
    print(""""1. If you guess the exact number, You'll get 20 points.
              2. If you guess the exact number on second guess, You'll get 10 points.
              3. If you guess the exact number on third guess, You'll get 5 points.
              4. If you guess the exact number on fourth guess, You'll get 3 points.
              5. If you guess the exact number on fifth guess, You'll get 1 points.
              Otherwise, you're not getting any points""")
else:
    print("Ok, Let's play the game.")
while is_running:
    guess = input("Enter your guess-:")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highes_num:
            print("That number is out of range :(")
            print(f"Please select a number between {lowest_num} and {highes_num}")
        elif guess > computer_guess:
            print("Too high. try again!")
        elif guess < computer_guess:
            print("Too low. try again!")
        else:
            print(f"CORRECT! The answer was {computer_guess}.")
            print(f"Number are guesses: {guesses}")
    else:
        print("invalid guess!")
        print(f"Please select a number between {lowest_num} and {highes_num}")
def points():
    if computer_guess == guess:
        print()
