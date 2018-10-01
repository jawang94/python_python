#1
def biggieSize(arr):
    for i in range(0,len(arr)):
        if(arr[i] >= 0):
            arr[i] = "big"
    return arr
x = [-1,2,-3,5]
print(biggieSize(x))

#2
def countPositives(arr):
    count = 0
    for i in range(0,len(arr)):
        if(arr[i] >= 0):
            count += 1
    arr[len(arr)-1] = count
    return arr
x = [1,2,-3,4,5]
print(countPositives(x))

#3
def sumTotal(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum += arr[i]
    return sum
x = [1,2,3,4,5]
print(sumTotal(x))

#4
def average(arr):
    sum = float(0)
    for i in range(0,len(arr)):
        sum += arr[i]
    return sum/len(arr)
x = [1,2,3,4]
print(average(x))

#5
def length(arr):
    return len(arr)
x = [1,2,3,4,5]
print(length(x))

#6
def minimum(arr):
    min = arr[0]
    if(len(arr) == 0):
        return False
    else:
        for i in range(0,len(arr)):
            if(arr[i] < min):
                min = arr[i]
    return min
x = [1,2,3,4,5,-3]
print(minimum(x))

#7
def maximum(arr):
    max = arr[0]
    if(len(arr) == 0):
        return False
    else:
        for i in range(0,len(arr)):
            if(arr[i] > max):
                max = arr[i]
    return max
x = [1,2,3,4,5,-1,12]
print(maximum(x))

#8
def ultimateAnalyze(arr):
    sumAvgMinMaxLen = {
        'sumTotal': 0,
        'minimum': arr[0],
        'maximum': arr[0],
        'length': len(arr)
    }
    for i in range(0,len(arr)):
        sumAvgMinMaxLen['sumTotal'] += arr[i]
        if(arr[i] < sumAvgMinMaxLen['minimum']):
            sumAvgMinMaxLen['minimum'] = arr[i]
        if(arr[i] > sumAvgMinMaxLen['maximum']):
            sumAvgMinMaxLen['maximum'] = arr[i]
    sumAvgMinMaxLen['average'] = float(sumAvgMinMaxLen['sumTotal']/len(arr))
    return sumAvgMinMaxLen
x = [1,2,3,4,5]
print(ultimateAnalyze(x))

#9
def reverseList(arr):
    temp = 0
    for i in range(0,len(arr)/2):
        temp = arr[i]
        arr[i] = arr[len(arr)-i-1]
        arr[len(arr)-i-1] = temp
    return arr
x = [1,2,3,4,5]
print(reverseList(x))


