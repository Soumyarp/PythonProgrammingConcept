def largestElement(lst):
    largest = lst[0]
    for i in range(0, len(lst)):
        if lst[i] > largest:
            largest = lst[i]
    return largest


def largestele(n):
    largest = n[0]
    for i in range(0,len(n)):
        largest=max(largest,n[i])
    return largest

arr=[55,32,-97,2,99,3,0,45,67,101]
print(largestele(arr))
print(largestElement(arr))