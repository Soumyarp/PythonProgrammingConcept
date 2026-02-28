def main(str):
    words = str.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)



str ="I love python programming"
main(str)

