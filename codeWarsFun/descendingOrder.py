def descending_order(num):
    output = ""
    numList = [int(digit) for digit in str(num)]
    for i in range(len(numList)):
        output = f"{output}{max(numList)}"
        numList.remove(max(numList))
    return int(output)
print(descending_order(51512))