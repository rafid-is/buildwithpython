import random
options = ("rock", "paper", "scissors")
print(options)

running = True

while running:
    playerChoice = None
    while playerChoice not in options:
        playerChoice = input("select a options: ")
    computerChoice = random.choice(options)
    print(f"Player Choose: {playerChoice}")
    print(f"Player Choose: {computerChoice}")
    if playerChoice == computerChoice:
        print("tie")
    elif playerChoice == "rock" and computerChoice == "scissors":
        print("You win!")
    elif playerChoice == "scissors" and computerChoice == "paper":
        print("You win!")
    elif playerChoice == "paper" and computerChoice == "rock":
        print("You win!")
    else:
        print("You lose!")
    #exit the game:
    if not input("play again?(y/n): ").lower() == "y":
        running = False
print("Exit! Thanks for playing.")
print("Did you enjoyed it?")
feedback = input()
if feedback == "yes":
    print("Thanks for sharing!")