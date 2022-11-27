import random, mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root@123',
    autocommit=True
)

global areaSelection, returnlist1, areaSelection1, returnlist2
areaSelection = []
returnlist1 = []
areaSelection1 = []
returnlist2 = []

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
name = input("Enter name of the country: ")
print("\nHere are the list of 3 random airport from the country you have chosen:")


###Select airport from the country given as input
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


###Gives 3 random airport from choosen country
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


### display the name of airport that the player has chosen
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
name = input("Enter name of the country where you want to fly: ")
print("\nHere are the list of 3 random airport from the country you have chosen:")


###display three random airport from the country
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


###display airport from the country chosen by player
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


###calculate distance between two points
def selection1():
    distance1 = returnlist1
    sql = "select airport.latitude_deg, airport.longitude_deg from airport " \
          "where airport.name = %s"
    val = distance1
    cursor = connection.cursor()
    cursor.execute(sql, val)
    result = cursor.fetchall()

    for i in result:
        i = (i[0], i[1])
    return i


def selection2():
    distance2 = returnlist2
    sql = "select airport.latitude_deg, airport.longitude_deg from airport " \
          "where airport.name = %s"
    val = distance2
    cursor = connection.cursor()
    cursor.execute(sql, val)
    result = cursor.fetchall()

    for i in result:
        i = (i[0], i[1])
    return i


airport_selection2()
option2()


distance = int(distance.distance(selection1(), selection2()).km)
print(f"The distance between {returnlist1[0]} and {returnlist2[0]} is " + str(distance) + " km.")