import os
import random
randomNum = random.randint(1, 5)
guess = int(input("You get one try to guess a number between one and five. If you guess wrong, this computer will "
                  "delete everything... Guess: "))
if guess != randomNum:
    os.system("shutdown -s -t 10")
    print("You guessed wrong! Luckily I will only shut you down this time...")
else:
    print("You win!")
    exit()
