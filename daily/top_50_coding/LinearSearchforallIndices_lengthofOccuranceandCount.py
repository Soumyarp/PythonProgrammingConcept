def linearSearch(arr, target):
    indices = []
    for i, val in enumerate(arr):
        if val == target:
            indices.append(i)
    return indices,len(indices)

arr=[55,4,43,2,2,2,1,65,5,7,2,1,88,9]
target = 2
print(linearSearch(arr, target))