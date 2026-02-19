def onetoNusingtailRecursion(i,n):
    if i>n:
        return

    print(i)
    onetoNusingtailRecursion(i+1, n)

onetoNusingtailRecursion(1,10)