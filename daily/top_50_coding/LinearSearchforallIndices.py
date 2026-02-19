def linearSearch(arr, target):
    indices = []
    n = len(arr)
    for i in range(0,n):
        if arr[i] == target:
            indices.append(i)
    # return indices if indices else -1  //instead of this one liner we can do the following if-else
    if indices:
        return indices
    else:
        return -1


arr=[55,4,43,2,2,2,1,65,5,7,2,1,88,9]
target = 100
print(linearSearch(arr, target))