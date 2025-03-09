def solution(number):
    counter = 0
    if(number<=0):
        return counter

    for i in range(number):
        if(i%3 == 0 or i%5==0):
            print(i)
            counter += i
    return counter
print(solution(10))

