def findFrequencyofList(lst):
    freq_map ={}
    for i in range(0, len(lst)):
        if lst[i] in freq_map:
            freq_map[lst[i]] += 1
        else:
            freq_map[lst[i]] = 1
    return freq_map

def findFrequencyofListusingi(lst):
    freq_map ={}
    for i in lst:
        if i in freq_map:
            freq_map[i] += 1
        else:
            freq_map[i] = 1
    return freq_map

arr=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,6]
print(findFrequencyofListusingi(arr))
print(findFrequencyofList(arr))