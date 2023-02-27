import random

options = ['rock', 'paper', 'scissors']
choice = None

print("Rock, Paper Scissors")
while choice not in options:
    choice = input("Enter your choice, rock, paper, scissors: ")

game = random.choice(options)

print(f"You choose: {choice}")
print(f"Game choose: {game}")

if choice == game:
    print("it's a tie")
elif choice == "rock" and game == "scissors":
    print("You Win")
elif choice == "paper" and game == "rock":
    print("You Win")
elif choice == "scissors" and game == "paper":
    print("You Win")
else:
    print("You Lose")