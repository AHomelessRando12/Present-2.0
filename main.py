import os
import random
import time
randomNum = random.randint(1, 5)
guess = int(input("You get one try to guess a number between one and five. If you guess wrong, this computer will "
                  "delete everything... Guess: "))
if guess != randomNum:
    print("You guessed wrong! Luckily I will only log you off this time...")
    time.sleep(5)
    os.system("logoff")
else:
    print("You win!")
    exit()
