import random
l=["rock","scissor","paper"]
'''
   rock vs paper -> paper wins
   rock vs scissor -> rock wins
   scissor vs paper -> scissor wins
   
   '''
while True:
    usercount=0
    computercount=0
    userchoice=int(input("""
    Game Start....
    1 Yes| Play
    2 No | Exist
    
    """))
    if userchoice==1:
        for a in range(1,6):
            userInput=int(input("""
                                 1 Rock
                                 2 Scissor
                                 3 Paper
                                 
                                 """))
            if userInput==1:
                userchoice="rock"
            elif userInput==2:
                userchoice="scissor"
            elif userInput==3:
                userchoice="paper"
            computerChoice=random.choice(l)
            if computerChoice==userchoice:
                print("Computer Value ",computerChoice)
                print("User Value ",userchoice)
                print("Game Draw")
                usercount=usercount+1
                computercount=computercount+1
            elif (userchoice=="rock" and computerChoice=="scissor") or (userchoice=="paper" and computerChoice=="rock")or (userchoice=="scissor" and computerChoice=="paper"):
                print("Computer Value ",computerChoice)
                print("User Value ",userchoice)
                print("You Win")
                usercount=usercount+1
            else:
                print("Computer Value ",computerChoice)
                print("User Value ",userchoice)
                print("Computer Win")
                computercount=computercount+1
        if usercount==computercount:
            print("Final Game is Draw...")
            print("Computer Score ",computercount)
            print("User Score ",usercount)
        elif usercount>computercount:
            print("Finally You Win the Game...")
            print("Computer Score ",computercount)
            print("User Score ",usercount)
        else:
            print("Finally Computer Win the Game...")
            print("Computer Score ",computercount)
            print("User Score ",usercount)
    else:
        break

