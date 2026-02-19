def checkPaliondrome(n):
    num =n
    rev=0
    while num>0:
        last_digit= num%10
        rev = rev*10+last_digit
        num =num//10
    return n == rev

def printPaliondrome(n):
    num =n
    rev =0
    while num>0:
        ld = num%10
        rev = rev*10+ld
        num=num//10
    if n==rev:
        print("paliondrome")
    else:
        print("not a paliondrome")


print(checkPaliondrome(12321))
printPaliondrome(7747383)
