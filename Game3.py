###To find treasure for Pro version
import random


def treasure():
    result = random.randint(1, 2)

    while True:
        lock = ["Abra", "Dabra", "Abra-Dabra"]
        chosen = random.choice(lock)
        print(chosen)

        if result == 1:
            print("Congratulation! You found the Treasure.\n")
            print("Choose the lock to open your treasure.")
            print(f"1. {lock[0]}")
            print(f"2. {lock[1]}")
            print(f"3. {lock[2]}\n")

            player1 = input("Enter number 1, 2, 3: ")

            if int(player1) == 1:
                if lock[0] == chosen:
                    print("Congratulation! You have unlocked the Treasure.")
                    print("Boom!!! 500 points")
                    break

                else:
                    print("OOPs! Wrong code.")
                    print("The correct code was *** " + chosen + " ***")
                    break

            elif int(player1) == 2:
                if lock[1] == chosen:
                    print("Congratulation! You have unlocked the Treasure.")
                    print("Boom!!! 500 points")
                    break

                else:
                    print("OOPs! Wrong code.")
                    print("The correct code was *** " + chosen + " ***")
                    break

            elif int(player1) == 3:
                if lock[2] == chosen:
                    print("Congratulation! You have unlocked the Treasure.")
                    print("Boom!!! 500 points")
                    break

                else:
                    print("OOPs! Wrong code.")
                    print("The correct code was *** " + chosen + " ***")
                    break

            else:
                print("Sorry, Wrong input.")
                break

        else:
            print("Unfortunately! No any Treasure. Try your luck in next destination.")
            break
    return


treasure()
