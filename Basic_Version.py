import random, mysql.connector


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root@123',
    autocommit=True
)


print("\n                                          ****************  Wel-Come To Game Treasure Hunt  ***************")
user = input("Enter Player Name: ")
print("Welcome to board " + user + "!\n")


user = input("How do you want to proceed ahead?"
        "\n 1.Start Game"
        "\n 2.Watch Tutorial\n ")

user = input("Choose difficulty level:"
             "\n1.Basic Version:"
             "\n2.Pro Version"
             "\n")
print("Let Play!")


def game():
    name = input("Enter name of the country: ")
    print("\nHere are the list of 3 random airport from the country you have chosen:")
    areaSelection = []
    returnlist1 = []
    areaSelection1 = []
    returnlist2 = []

    def locations():
        sql = "select airport.name from airport " \
              "inner join country on airport.iso_country=country.iso_country " \
              "where country.name='" + name + "'"

        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        airports = []
        for x in range(len(result)):
            airports.append(result[x][0])
        return airports

    def airport_selection1():
        airport = locations()
        chosen = random.sample(airport, 3)
        print(f"1. {chosen[0]}")
        areaSelection.append(chosen[0])
        print(f"2. {chosen[1]}")
        areaSelection.append(chosen[1])
        print(f"3. {chosen[2]}\n")
        areaSelection.append(chosen[2])
        return areaSelection

    def option1():
        chosen = areaSelection
        while True:
            player = input("Enter number from the list of airport of your choice: ")

            if int(player) == 1:
                print(f"You have chosen {chosen[0]}.\n")
                returnlist1.append(chosen[0])
                break

            elif int(player) == 2:
                print(f"You have chosen {chosen[1]}.\n")
                returnlist1.append(chosen[1])
                break

            elif int(player) == 3:
                print(f"You have chosen {chosen[2]}.\n")
                returnlist1.append(chosen[2])
                break

            else:
                print(f"OOPs! Wrong input.")
                break
        return returnlist1

    airport_selection1()
    option1()

    i = 0
    while i < 5:
        name = input("\nEnter name of the country where you want to fly: ")
        print("\nHere are the list of 3 random airport from the country you have chosen:")

        def airport_selection2():
            airport = locations()
            chosen = random.sample(airport, 3)
            print(f"1. {chosen[0]}")
            areaSelection1.append(chosen[0])
            print(f"2. {chosen[1]}")
            areaSelection1.append(chosen[1])
            print(f"3. {chosen[2]}\n")
            areaSelection1.append(chosen[2])
            return areaSelection1

        def option2():
            chosen = areaSelection1
            while True:
                player = input("Enter number from the list of airport of your choice: ")

                if int(player) == 1:
                    print(f"You have chosen {chosen[0]}.\n")
                    returnlist2.append(chosen[0])
                    break

                elif int(player) == 2:
                    print(f"You have chosen {chosen[1]}.\n")
                    returnlist2.append(chosen[1])
                    break

                elif int(player) == 3:
                    print(f"You have chosen {chosen[2]}.\n")
                    returnlist2.append(chosen[2])
                    break

                else:
                    print(f"OOPs! Wrong input.")
                    break
            return returnlist2

        areaSelection1.clear()
        returnlist2.clear()

        def treasure():
            result = random.randint(1, 2)
            Total_score = 0

            if result == 1:
                print("Congratulation! You found the Treasure.")
                print("You got 500 points.")

                Total_score += 500
                print("Your score is " + str(Total_score))


            else:
                print("Unfortunately! No any Treasure. Try your luck in next destination.")
                print("no points.")
                score = 0
                Total_score += 0
                print("Your score is " + str(Total_score))

        airport_selection2()
        option2()
        treasure()
        i += 1


game()





