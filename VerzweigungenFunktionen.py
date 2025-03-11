#1

def isPositive(zahl):
    if(zahl>0):
        return True
    else:
        return False

print(isPositive(4))
print(isPositive(-1))

#2

def evenNumber(number):
    if (number%2 == 0):
        return True
    else:
        return False

print(evenNumber(3))


#3

def isMature(age):
    if(age >= 18):
        return True
    else:
        return False
print (isMature(19))
print(isMature(10))

#4

def grading(points):
    if(points>=90):
        return "Sehr gut"
    elif(points>=80):
        return "Gut"
    elif(points>=70):
        return "Befriedigend"
    elif(points>=60):
        return "Ausreichend"
    else:
        return "Nicht bestanden"

def temperatureRating(temp):
    if(temp>30):
        return "Es ist heiß"
    elif temp<30 and temp>20:
        return "wetter ist angenehm"
    else:
        return "Es ist kalt"