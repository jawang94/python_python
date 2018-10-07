#JAVASCRIPT SOLUTION:
# function insertSort(arr){
#   for(var i=0 ; i<arr.length ; i++){
#     let value = arr[i];
#     for(var j=i-1 ; j>=0 && arr[j] > value ; j--){
#       arr[j+1] = arr[j];
#     }
#     arr[j+1] = value;
#   }
#   return arr;
# } 

let coolarr = [1,5,7,3,6];
insertSort(coolarr);

def insertSort(arr):
    for i in range(0,len(arr)):
        value = arr[i]
        for j in range(i-1,-1):
            if arr[j] > value:
                arr[j+1] = arr[j]
        arr[j+1] = value
    return arr

coolarr = [1,5,7,3,6]
insertSort(coolarr)