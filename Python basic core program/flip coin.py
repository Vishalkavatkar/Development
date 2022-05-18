from random import randint 
from time import sleep

flip = int(input("How many times you want to flip the coin? :"))

for i in range (flip):
    result = randint(0,1)
    sleep(1)
    # print(result)
    if result == 0:
        print("Heads")
    else:
        print("Tails")