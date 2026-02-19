def checkArrayorListisSorter(arr):
    for i in range (0,len(arr)-1):
        if arr[i]<arr[i+1]:
            return True
        else:
            return False


arr = [1, 2, 3, 4, 5, 6]
print(checkArrayorListisSorter(arr))