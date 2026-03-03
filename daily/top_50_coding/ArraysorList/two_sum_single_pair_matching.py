def two_sum(numbers, target):
    memory={}
    for index,number in enumerate(numbers):
        match= target - number
        if match in memory:
            return [memory[match],index]
        memory[number]=index

if __name__ == '__main__':
    numbers = [4,3,7,2,9]
    target =11
    result =two_sum(numbers,target)
    print(result)