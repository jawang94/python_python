def insertSort(arr):
    for i in range(1,len(arr)):
        value = arr[i]
        j = i-1
        while j >= 0 and value < arr[j]:
          arr[j+1] = arr[j]
          j -= 1
        arr[j+1] = value
    return arr

coolarr = [1,5,7,3,6]
print(insertSort(coolarr))