#1
# print ("Hallo, Python-Welt!")
# print("Ich lerne gerade Python.")
# print("Programmieren macht Spaß!")

#2
# print("name: Max Mustermann\nBeruf:\tSoftwareentwickler\nWohnort: Hamburg ")

#3
# def greetUser():
#     userName = input("hey what is your name?\n ")
#     return f"welcome to the club {userName}"
# print(greetUser())

#4
# def sumOfTwo():
#     int1 = int(input("value1?"))
#     int2 = int(input("value2?"))
#     return int1+int2
#
# print(sumOfTwo())

#5
# article = "Laptop"
# price = 999.99
# pieces = 3
# totalPrice = price*pieces
#
# print(f"Artikel: {article}\nPreis:{price}€\nMenge:{pieces}\nGesamtpreis:{totalPrice:.2f}€")

#6
# def euroToDollar(euro):
#     wechselkurs = 1.1
#     dollar = euro*wechselkurs
#     return dollar
#
# print(euroToDollar(2))

#7
currentYear = 2025
def getting100():
    global currentYear
    currentAge = int(input("how old are you"))
    yearsTo100 =  100 - currentAge
    return f"you will reach an age of 100 in the year {currentYear+yearsTo100}"
print(getting100())

