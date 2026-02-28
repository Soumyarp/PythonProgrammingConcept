def LowertoUpper(str):
    results = ""
    for char in str:
        if 'a'<char<'z':
           results+= chr(ord(char) - 32)
        else:
            results += char
    print(results)


def UppertoLower(str):
    results = ""
    for char in str:
        if 'A'<char<'Z':
           results+= chr(ord(char) + 32)
        else:
            results += char
    print(results)

str = "hello"
LowertoUpper(str)
str2= "WORLD"
UppertoLower(str2)