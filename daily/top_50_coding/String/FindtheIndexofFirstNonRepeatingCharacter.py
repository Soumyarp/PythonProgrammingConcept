def findindexofnonrepeatingchar(str):

    freq_map= dict()
    for char in str:
        if char in freq_map:
            freq_map[char]+=1
        else:
            freq_map[char] =1
    print(freq_map)

    for key,value in freq_map.items():
        if value ==1:
            print(str.index(key))
            break

str= "swiss"
findindexofnonrepeatingchar(str)