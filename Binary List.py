import math as m
def binaryList(lis):
    newList = []
    for i in range(len(lis)):
        newList.append(lis[i]%2)
    return newList

def toBase10(lis):
    num = 0
    negative = False
    if(lis[0] == 1):
        negative = True
        for i in range(len(lis)):
            if(lis[i] == 1):
                lis[i] = 0
            else:
                lis[i] = 1
        addOne(lis)
    for i in range(len(lis)):
        digit = lis[len(lis)-1-i]
        newDigit = digit * m.pow(2,i)
        num += newDigit
    if(negative):
        num = 0 - num
    return int(num)

def addOne(lis):
    i = len(lis) - 1
    done = False
    while(not done):
        if(lis[i] == 0):
            lis[i] = 1
        else:
            lis[i] = 0
        i -= 1
        if((i < 0) or (lis[i + 1] == 1)):
            done = True
    return lis

print(binaryList([10,5,3,4,8]))
print(toBase10(binaryList([10,5,3,4,8])))
