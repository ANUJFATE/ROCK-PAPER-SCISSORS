import random
player_score = 0
computer_score = 0
rounds = int(input("computer : how many do wan to play : "))
for i in range(rounds):
    computer = random.choice(("rock","paper","scissors"))
    print("computer choice   :",computer)
    playerchoise = input("enter your choice (paper,rock,scissors) : ")
    if(playerchoise == computer):
        print("draw")
    elif(playerchoise == "rock" and computer== "scissors"):
        print("player is win")
        player_score += 1
    elif(playerchoise == "paper" and computer == "rock"):
        print("player is win!")
        player_score += 1
    elif(playerchoise == "scissors" and computer == "paper"):
        print("player is win")
        player_score += 1
    elif(computer == "scissors" and playerchoise == "paper"):
        print("computer is win ")
        computer_score += 1
    elif(computer == "rock" and playerchoise == "scissors"):
        print("computer is win")
        computer_score += 1
    elif(computer == "paper" and playerchoise == "rock"):
        print("computer is win ")
        computer_score += 1
    else:
        print("invalid")
print("\nfinal score")
print("player : ", player_score)
print("computer : ",computer_score)
if player_score > computer_score:
    print("player  won this match")
elif(computer_score > player_score):
    print("computer won this match")
else:
    print("match draw")
       
    


 
        
    
    
   
    