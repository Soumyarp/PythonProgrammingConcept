def stringCompression(s):
    results = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            results.append(s[i-1] + str(count))
            count = 1
    results.append(s[-1] + str(count))
    print("".join(results))


s = "aaabbccc"
stringCompression(s)

