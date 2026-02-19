def linearSearch(arr, target):
    n = len(arr)
    for i in range(0,n):
        if arr[i] == target:
            return i
    return -1

arr=[55,4,43,2,2,2,1,65,5,7,2,1,88,9]
target = 2
print(linearSearch(arr, target))