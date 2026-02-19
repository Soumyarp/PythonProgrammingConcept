def armstringNumber(n):
    num =n
    nod = len(str(n))
    result=0
    for i in range(0, nod):
        ld = num%10
        result=ld**nod+result
        num=num//10
    print(result)
def armstrongNum(n):
    num =n
    result=0
    nod= len(str(n))
    while num>0:
        ld=num%10
        result = result+(ld**nod)
        num=num//10
    return result

print(armstrongNum(1634))
armstringNumber(153)
