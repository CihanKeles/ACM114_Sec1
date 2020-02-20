Rock_Paper_Scissors = ["Rock", "Paper", "Scissors"]
import random
rock = Rock_Paper_Scissors[0]
paper = Rock_Paper_Scissors[1]
scissors = Rock_Paper_Scissors[2]
userInput=input("Enter your choice --> Rock? Paper? or Scissors? Which one? ")
randComp = random.choice(Rock_Paper_Scissors)

print("Computer made the choice --> ", randComp)
if userInput == paper:
	if paper == randComp:
		print("DRAW!")
	elif rock == randComp:
        	print("You Win!")
	elif scissors == randComp:
        	print("You Lose! Computer Wins!")

elif userInput == rock:
    	if rock == randComp:
        	print("DRAW!")
    	elif paper == randComp:
        	print("You Lose! Computer Wins!")
    	elif scissors == randComp:
        	print("You Win!")

elif userInput == scissors:
    	if scissors == randComp:
        	print("DRAW!")
    	elif rock == randComp:
        	print("You Lose! Computer Wins!")
    	elif paper == randComp:
        	print("You Win!")

else:
	print("Hey! I think you missed to enter the right choice. Plese try again!! You will enjoy :)")
	userInput=input("Enter your choice --> Rock? Paper? or Scissors? Which one? ")
	