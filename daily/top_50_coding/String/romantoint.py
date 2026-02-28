def romantoint(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0
    for char in reversed(s):
        curr_val= roman_numerals[char]
        if curr_val<prev_value:
            total -= curr_val
        else:
            total+= curr_val
        prev_value = curr_val
    return total


s = "MCMXCIV"
print(romantoint(s))