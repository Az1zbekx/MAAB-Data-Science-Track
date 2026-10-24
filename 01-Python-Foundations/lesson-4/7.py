import random

x, y = 0, 0
while True:
    computer = random.choice(["rock", "paper", "scissors"])
    player = input().lower()
    if (computer == "rock" and player == "scissors") or (computer == "paper" and player == "rock") or (computer == "scissors" and player == "paper"):
       x += 1
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
       y += 1
    print(computer, ":", player)
    print(x, y)
    if x == 5:
        print("Computer Win!")
        break
    elif y == 5:
        print("Player Win!")
        break

    
