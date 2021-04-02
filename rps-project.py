import random
while True:
    choose=input("Choose from the following: rock, paper, scissors: ")
    choose = choose.lower()
    
    if choose == "quit":
        print("game over")
        break

    if choose != "rock" and choose != "paper" and choose != "scissors":
        print("choose again")
        continue

    com_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose :{com_choice}")

    if choose == com_choice:
        print("game tied!")
        continue
    elif choose == "paper" and com_choice == "rock":
        print("you win")
        break
    elif choose == "scissors" and com_choice == "paper":
        print("you win")
        break
    elif choose == "rock" and com_choice == "scissors":
        print("you win")
        break
    else: 
        print("You lose")
    