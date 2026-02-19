# n=2578
# count=0
# num=n
# while num>0:
#     count+=1
#     num =num//10
# print(count)

def countofDigits(n):
    num =n
    count=0
    while num>0:
        count=count+1 #count+=1
        num=num//10
    return count

print(countofDigits(567893))