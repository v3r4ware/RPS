import random 
import os

USERNAME = os.environ.get('USERNAME')

user_wins = 0 
computer_wins = 0

user_options = ["rock", "paper", "scissors"] 
computer_options = ["rock", "paper", "scissors"] 

print(r"""
  _____            _      _____                         _____      _                        _  
 |  __ \          | |    |  __ \                       / ____|    (_)                      | | 
 | |__) |___   ___| | __ | |__) |_ _ _ __   ___ _ __  | (___   ___ _ ___ ___  ___  _ __ ___| | 
 |  _  // _ \ / __| |/ / |  ___/ _` | '_ \ / _ \ '__|  \___ \ / __| / __/ __|/ _ \| '__/ __| | 
 | | \ \ (_) | (__|   <  | |  | (_| | |_) |  __/ |     ____) | (__| \__ \__ \ (_) | |  \__ \_| 
 |_|  \_\___/ \___|_|\_\ |_|   \__,_| .__/ \___|_|    |_____/ \___|_|___/___/\___/|_|  |___(_) 
                                    | |                                                        
                                    |_|                                                                             
    """)
print("=====================================================================================================================")
user_input = input("Hello " + USERNAME +"! "
                    "I think you know how to play rock paper scissors but just in case, here are the rules: \n"
                    "Rock beats Scissors \n"
                    "Scissors beats Paper \n"
                    "Paper beats Rock \n" 
                    
                    "Press ENTER to continue \n")
print("=====================================================================================================================")

while True: 
            
    user_input = input("Type either Rock, Paper or Scissors to play! ").lower()
    if user_input == "q":
        break   

    if user_input not in user_options:  
        continue

    random_number = random.randint(0, 2)
    # rock is 0, paper is 1, scissors is 2 in the list array, learnt in lesson 2 of python class 
    computer_pick = computer_options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1  
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")

print("The computer won", computer_wins, "times.")

print("Goodbye " + USERNAME + "!")
exit()
