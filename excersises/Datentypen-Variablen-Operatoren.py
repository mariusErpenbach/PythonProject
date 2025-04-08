#1
from xmlrpc.client import Boolean

age = 100
height = 1.94
name = "Marius"
isThisTrue = False

print(f"{name} is {age} years old and about {height} in height. This is {isThisTrue}")

#2
ageString = str(age)
heightInt = int(height)
nameNumber = Boolean(name) # a string that wasnt empty is "True" as an Boolean
isThisTrueString = str(isThisTrue)

print(f"{nameNumber} is {ageString} years old and about {heightInt} in height. This is {isThisTrueString}")

#3

# def multiplyNumberByTen():
#     userName = input("Hello, what is your name?\n")
#     userAge = input("how old are you, friend?\n")
#     print(f"Hallo {userName}, das Ergebnis ist {int(userAge)*10}")
#
# multiplyNumberByTen()

#4
# print(15 + 7)
# print(100 - 45)
# print(8 * 6)
# print(81 / 9)
# print(10 % 3)
# print(2 ** 5)
# print(23 // 5)

#5

# temperatures = [int(input("value 1: ")), int(input("value 2: ")), int(input("value 3: "))]
# def average(list):
#     return sum(list) / len(list)
# print(f"{average(temperatures)} is the average temperature")

# import statistics
# print(f"average temperature is: {statistics.mean(temperatures)}")

#6

iq = int(input("whats your intelligence quotient: "))
tel = "0163"
int(tel)
booleanFalse = False
booleanTrue = True

print(f"iq:{iq},\n telNumber as int: {tel},\n Boolean False as int:{int(booleanFalse)},\n Boolean True as int:{int(booleanTrue)}")
