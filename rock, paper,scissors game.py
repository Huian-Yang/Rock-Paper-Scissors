import random #import the random module

while True: #keep looping until broken 
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices) #computer randomly chooses one
    player = None   #set to None for now until player input

    while player not in choices: #will keep looping until the player inputs 1 of the three choices
        player = input("rock, paper, or scissors?: ").lower() #player input + makes response all lower case

    if player == computer:    #tie situation
        print("Computer: ",computer)
        print("Player: ",player)
        print("Tie!")
    elif player == "rock":   #player using rock
        if computer == "paper": #computer use paper
            print("Computer: ",computer)
            print("Player: ",player)
            print("You lose!")
        if computer == "scissors": #computer use scissors
            print("Computer: ",computer)
            print("Player: ",player)
            print("You win!")
    elif player == "scissors": #player use scissors
        if computer == "paper": #computer use paper
            print("Computer: ",computer)
            print("Player: ",player)
            print("You win!")
        if computer == "rock": #computer use rock
            print("Computer: ",computer)
            print("Player: ",player)
            print("You lose!")
    elif player == "paper":  #player use paper
        if computer == "rock": #computer use rock
            print("Computer: ",computer)
            print("Player: ",player)
            print("You win!")
        if computer == "scissors": #computer use scissors
            print("Computer: ",computer)
            print("Player: ",player)
            print("You lose!")
            
    play_again = input("Play again? (yes/no): ").lower() #prompts the player to play again
    
    if play_again !="yes": #inputing values that are not "yes" will break the while loop
        break
    
print("Bye!") #print at last when while loop breaks  
        