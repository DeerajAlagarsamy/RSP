import random

user_wins = 0
comp_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input('\033[0m'+"1-Rock  2-Paper  3-Scissors  q-quit: "+'\033[0m').lower() 
    if user_input == "q":
        break
    elif user_input == "":
        continue    
    elif int(user_input) > len(options):
        continue
    user_input=options[int(user_input)-1]
    comp_input = options[random.randint(0,2)]
    
    print("You: ",user_input)
    print("System: ",comp_input)
    if user_input == comp_input:
        print('\033[93m'+"Match Draw!!!"+'\033[93m')
        continue
    elif user_input == "rock" and comp_input == "paper":
            print('\033[91m'+"You Loose..."+'\033[91m')
            continue
    elif user_input == "scissors" and comp_input == "rock":
            print('\033[91m'+"You Loose..."+'\033[91m')
            continue
    elif user_input == "paper" and comp_input == "scissors":
            print('\033[91m'+"You Loose..."+'\033[91m')
            continue
    else:
         print('\033[92m'+"You Win!!!"+'\033[92m')
         continue   
          
print('\033[94m'+"Goodbye"+'\033[94m')

