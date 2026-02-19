def stringFrequrecies(s):
    freq_map= dict() # create a dictionary to store the frequency of each character and can be used to check if a character has been seen before and we can use {} also instead of dict()
    for char in s:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1
    return freq_map

str = "hello world"
print(stringFrequrecies(str))