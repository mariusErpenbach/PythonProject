# #1
#
# counterA = 1
#
# while counterA <= 10:
#     print (counterA)
#     counterA +=1

# zahl = int(input("enter your number to add or 0 to stop"))
# summe = 0
# while zahl:
#     summe += zahl
#     zahl = int(input("enter your number to add or 0 to stop"))
# print(summe)

#2

# counterB = 0
# active = True
# while active:
#     number = int(input("enter a number"))
#     if number == 0:
#         active = False
#         print (counterB)
#     else:
#         counterB += number

#3
# myPassword = 12345
# loggedIn= False
# while not loggedIn:
#     passwordInput = input("enter your password: ")
#     if passwordInput==myPassword:
#         loggedIn = True
#         print("logged in")

#4
# for i in range(10):
#     print (i+1)

#5
# for i in range(22):
#     if i%2==0 and i != 0:
#         print(i)
# print("-"*20)
# for i in range(21):
#     if i%5==0 and i != 0:
#         print(i)

# for i in range(0,22,+2):
#     print(i)


#6

# for i in range(5):
#     print("*"*5)

#7
# for i in range(10,0,-1):
#     print(i)
# for i in range(10):
#     print(10-i)

#8
#
# friends = ["Anna","Max","Tom","Lisa"]
# friends.append("Marie")
# friends.remove("Tom")
# print (len(friends))

# #9

# #10
# orderedNumbers = [1,2,3,4,5]
# orderedNumbers.insert(len(orderedNumbers),6)
# orderedNumbers.insert(0,0)
# print (orderedNumbers)
#

#11
# for i in range(5):
#     print ((i+1)*10)

# lottozahlen=[10,20,30,40,50]
# for i in lottozahlen:
#     print(i)

#12
# prices = [3,4,1,2]
# sum = 0
# for i in range(len(prices)):
#     sum += prices[i]
#
# print (sum)

#13
# exampleString = "Marius"
# for i in range(len(exampleString)):
#     print (exampleString[i])

#14
# randomList = [1,2,3,4,5,11,14,15,16,6,7,8]
# for i in range (len(randomList)):
#     if randomList[i]<10:
#         print (randomList[i])

#15
# randomList = [1,2,3,4,5,11,14,15,16,6,7,8]
# for i in range(len(randomList)):
#     print(str(i) + "=" + str(randomList[i]))
#
#
# for index, item in enumerate(randomList):
#     print(index, item)
#
