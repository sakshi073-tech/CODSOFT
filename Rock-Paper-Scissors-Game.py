series = int(input("Enter the rounds: "))
rock_count = 0
paper_count = 0
scissor_count = 0

for i in range(series):
    player1 = input("Enter your choice(R,S,P): ").upper()
    player2 = input("Enter your choice(R,S,P): ").upper()

    if player1 == player2:
        print("Match is draw")
    elif (player1 == "R" and player2 == "S") or (player1 == "S" and player2 == "R"):
        print("Rock beats Scissor")
        rock_count += 1
    elif (player1 == "P" and player2 == "S") or (player1 == "S" and player2 == "P"):
        print("Scissor beats Paper")
        scissor_count += 1
    elif (player1 == "P" and player2 == "R") or (player1 == "R" and player2 == "P"):
        print("Paper beats Rock")
        paper_count += 1
    else:
        print("Invalid")

