#page 553
#2
def lowerValueOfTwo(a,b):
    valueList = [a,b]
    return min(valueList)

print(lowerValueOfTwo(5,3))

#3
def lowerValueOfThree(a,b,c):
    valueList = [a,b,c]
    return min(valueList)

print(lowerValueOfThree(5,3,7))

#4
def evenNumber(number):
    if (number%2 == 0):
        return True
    else:
        return False

print(evenNumber(3))

#5
def schaltJahr(year):
    if(year%4 == 0 and year%100!=0 or year%4 == 0 and year%100==0 and year%400==0 ):
        return True
    else:
        return False

print(schaltJahr(2000))