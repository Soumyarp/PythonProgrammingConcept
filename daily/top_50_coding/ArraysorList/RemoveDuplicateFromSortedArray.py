
def removeDuplicateFromSortedArray(arr):
    freq_map = {}
    for i in arr:
        if i in freq_map:
            freq_map[i] =0
        else:
            freq_map[i]=1
    for key,value in freq_map.items():
         if key!=0:
             print(key)


def removeDuplicateFromSortedArrayusingreturn(arr):
    freq_map = {}
    for i in arr:
        if i in freq_map:
            freq_map[i] += 1
        else:
            freq_map[i] = 1

    # Collect elements that appear only once
    uniques = []
    for key, value in freq_map.items():
        if key !=0:
            uniques.append(key)

    return uniques  # <-- return instead of print


arr=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,6]
print(removeDuplicateFromSortedArrayusingreturn(arr))
removeDuplicateFromSortedArray(arr)

