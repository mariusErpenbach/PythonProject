#1
#
# counterA = 10
#
# while counterA:
#     print (counterA)
#     counterA -=1

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

#6

# for i in range(5):
#     print("*"*5)

#7
# for i in range(10):
#     print(10-i)

#8
#
# friends = ["Anna","Max","Tom","Lisa"]
# friends.append("Marie")
# friends.remove("Tom")
# print (len(friends))

# #9
# randomNumbers = [5,3,8,1,2]
# randomNumbers.sort()
# print (randomNumbers)
#
# #10
# orderedNumbers = [1,2,3,4,5]
# orderedNumbers.insert(-1,6)
# orderedNumbers.insert(0,0)
# print (orderedNumbers)
# print ("3 is " + orderedNumbers.count(3) + "times in the list")
#

#11

# for i in range(5):
#     print ((i+1)*10)

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
randomList = [1,2,3,4,5,11,14,15,16,6,7,8]
for i in range(len(randomList)):
    print(str(i) + "=" + str(randomList[i]))


for index, item in enumerate(randomList):
    print(index, item)

