x = [1,5,3,4,67,8,2,6,]
def selectionSort(arr):
  for i in range(len(arr)):  #identifies each index of an arr
    for j in range(len(arr)):  #first loop is used to grab a unique index of the arr. This second loop then takes the unique index and runs a comparison parse through the remaining arr indices
      if arr[j] > arr[i]:  #if an index of the remaining indices is greater than the current min (arr[i])
        arr[i], arr[j] = arr[j], arr[i]  #if found, flip the positions of the greater value and the minimum value

  print(arr)

selectionSort(x)