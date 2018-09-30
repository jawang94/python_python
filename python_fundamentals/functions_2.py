#1
def countDown(num):
    arr = []
    for count in range(num,0,-1):
        arr.append(count)
    print(arr)
x = 5
countDown(x)

#2
def printAndReturn(arr):
    print(arr[0])
    return(arr[1])
x = [1,2]
printAndReturn(x)

#3
def firstPlusLength(arr):
    x = arr[0] + len(arr)
    return x
x = [1,2,3,4,5]
print(firstPlusLength(x))

#4
def greaterThanSecond(arr):
    newarr = []
    x = 0
    for i in range(0,len(arr)):
        if(len(arr) < 2):
            return False
        elif(arr[i] > arr[1]):
            newarr.append(arr[i])
            x += 1
    print(x)
    return newarr
x = [1,2,3,4,5,1234124,124,12,1]
greaterThanSecond(x)

#5
def lengthAndValue(size,value):
    arr = []
    for i in range(0,size):
        arr.append(value)
    return arr
print(lengthAndValue(4,7))

