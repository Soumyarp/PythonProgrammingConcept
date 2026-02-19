def factors(n):
    num =n
    result =[]
    for i in range(1,num+1):
        if num%i ==0:
            result.append(i)
    return result

print(factors(10))
