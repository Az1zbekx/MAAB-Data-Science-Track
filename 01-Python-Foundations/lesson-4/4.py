import random

while True:
    x = random.randint(0, 100)
    for t in range(10):
        n = int(input())
        if n > x:
            print("Too high!")
        elif n < x:
            print("Too low!")
        else:
            print("You guessed it right!")
            break
    else:  
        print("You lost. Want to play again?")
        if input().lower() not in ['y', 'yes', 'ok']:
            break
        continue
    break
