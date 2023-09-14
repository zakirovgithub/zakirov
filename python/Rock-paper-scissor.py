import time
import random

def timeSleep():
    print("1..", end="", flush=True)
    time.sleep(1)
    print("2..", end="", flush=True)
    time.sleep(1)
    print("3..", flush=True)
    time.sleep(1)
    
print("|---Rock-Paper-Scissors game---|")
readiness = input("Are you ready? y/n: ")

choices = ['rock', 'paper','scissor']
computer_answer = random.choice(choices)

if readiness == 'y':
    timeSleep()
    player_answer = input("Your answer(rock/paper/scissor): ")
    
    if computer_answer == player_answer:
        print("Computer chose: ", computer_answer)
        print("Player chose: ", player_answer)
        print("Tie")
    elif player_answer == "rock":
        print("Computer chose: ", computer_answer)
        print("Player chose: ", player_answer)
        if computer_answer == "paper":
            print("Computer wins!")
        elif computer_answer == "scissor":
            print("You win!")
    elif player_answer == "paper":
        print("Computer chose: ", computer_answer)
        print("Player chose: ", player_answer)
        if computer_answer == "scissor":
            print("Computer wins!")
        elif computer_answer == "rock":
            print("You win!")
    elif player_answer == "scissor":
        print("Computer chose: ", computer_answer)
        print("Player chose: ", player_answer)
        if computer_answer == "rock":
            print("Computer wins!")
        elif computer_answer == "paper":
            print("You win!")
    else:
        print("Wrong answer.")