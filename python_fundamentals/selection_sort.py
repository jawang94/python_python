#Initial Solution (arguably not even a solution but it works)
x = [1,5,3,4,67,8,2,6,]
def selectionSort(arr):
  for i in range(len(arr)):  #identifies each index of an arr
    for j in range(len(arr)):  #first loop is used to grab a unique index of the arr. This second loop then takes the unique index and runs a comparison parse through the remaining arr indices
      if arr[j] > arr[i]:  #if an index of the remaining indices is greater than the current min (arr[i])
        arr[i], arr[j] = arr[j], arr[i]  #if found, flip the positions of the greater value and the minimum value

  print(arr)

selectionSort(x)

#Refactored Solution (that makes way more sense)
arr = [1,5,5,1,57,7,21,5,47,7,2,0]

def selectionSort2(x):
  for i in range(len(x)):  #interating through the array, one index at a time
    min_index = i  #the position within the array of the smallest #
    for j in range(i+1, len(x)):  #iterating through the remaining array
      if x[min_index] > x[j]:  #if an integer is located within the remaining arr that is less than the current arr[i] integer,
        min_index = j  #we set the location of that integer to equal the min_index (location of smallest #). This second loop will keep going until the end of the remaining array length, constantly setting a new min_index (if there are any)
    x[i], x[min_index] = x[min_index], x[i]  #once second loop is finished, the first loop will take the position of the current index [i] and swap the integer with the finalized minimum index [j] aka min_index
  return x  #finally, we return the sorted array

print(selectionSort2(arr))
