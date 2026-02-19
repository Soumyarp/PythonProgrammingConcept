# Identifying substring index no from a given String
def implementstrStr(mainString:str, subString:str) -> int:
    if subString == "":
        return 0
    if len(subString) > len(mainString):
        return -1
    for i in range(len(mainString) - len(subString) +1):
        if mainString[i:i+len(subString)] == subString :
            return i
    return -1

mainString = "ababcabc"
subString = "abcab"
print(implementstrStr(mainString,subString))


