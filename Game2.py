###To find treasure for basic version
import random


def treasure():
    result = random.randint(1, 2)
    while True:
        if result == 1:
            print("Congratulation! You found the Treasure.")
            break

        else:
            print("Unfortunately! No any Treasure. Try your luck in next destination.")
            break
    return


treasure()

