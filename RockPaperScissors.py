import random

#Bot choices
rps = ["Rock", "Paper", "Scissors"]
bot_choice = random.choice(rps)

#Game start
print("RULES: Rock > Scissors|Paper > Rock|Scissors > Paper")
question = input("Would you like to play?(Y/N) ")


if question == "Y":
    player_choice = input("Rock, Paper, Scissors: ")
else:
    print("Goodbye")
    quit()

#Rock
if player_choice == "Rock" and bot_choice == "Scissors":
    print("You Win!")
    print("Bot's choice: " + bot_choice)
elif bot_choice == "Rock" and player_choice == "Scissors":
    print("You Lose!")
    print("Bot's choice: " + bot_choice)
    quit()

#Paper
if player_choice == "Paper" and bot_choice == "Rock":
    print("You Win!")
    print("Bot's choice: " + bot_choice)
elif bot_choice == "Paper" and player_choice == "Rock":
    print("You Lose!")
    print("Bot's choice: " + bot_choice)
    quit()

#Scissors
if player_choice == "Scissors" and bot_choice == "Paper":
    print("You Win!")
    print(bot_choice)
elif bot_choice == "Scissors" and player_choice == "Paper":
    print("You Lose!")
    print("Bot's choice: " + bot_choice)
    quit()

#Tie
if player_choice and bot_choice == "Rock":
    print("Tie!")
if player_choice and bot_choice == "Paper":
    print("Tie!")
if player_choice and bot_choice == "Scissors":
    print("Tie!")
