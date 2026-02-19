def reverseNum(n):
    num =n
    rev=0
    while num >0:
        ld= num%10
        rev= rev*10+ld
        num=num//10
    return rev

def reverseaNum(n):
    num =n
    rev =0
    while num>0:
        ld= num%10
        rev =rev*10+ld
        num=num//10
    print(rev)

reverseaNum(12345)
print(reverseNum(87657))