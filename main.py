comp=0
user=0
print("Enter 1 for stone \nEnter 2 for paper \nEnter 3 for scissor")
while True:
    i=input("Enter Your Option: ")
    if i=="1":
        u="stone"
    elif i=="2":
        u="paper"
    elif i=="3":
        u="scissor"
    else:
        print("Wrong Input")
        continue
    import string
    import random
    WORDS = ("stone", "paper", "scissor")
    c= random.choice(WORDS)
    print(f"Computer: {c}")
    print(f"User: {u}")
    if u == c:
        print("Tie")
        comp+=1
        user+=1
    elif u == "stone" and c== "paper":
        print("Computer Wins")
        comp+=1
    elif u== "stone" and c== "scissor":
        print("User Wins")
        user+=1
    elif u == "paper" and c== "stone":
        w2=print("User Wins")
        user+=1
    elif u == "paper" and c== "scissor":
        w1=print("Computer Wins")
        comp+=1
    elif u == "scissor" and c== "stone":
        w1=print("Computer Wins")
        comp+=1
    elif u == "scissor" and c== "paper": 
        w2=print("User Wins")
        user+=1
    w=input("****Enter y to continue and n to exit****")
    if w== "n":  
        print(f"Your score is {user} and computer score is {comp}")
        if comp>user:
            print("Computer wins")
        elif comp<user:
            print("You win")
        else:
            print("Draw")
        break
    else:
        continue

        
      