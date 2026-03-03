def all_two_sums(nums, target):
    memoryview ={}
    results =[]
    for index, num in enumerate(nums):
        match = target - num
        if match in memoryview:
            results.append([memoryview[match], index])
        memoryview[num]=index
    return results

if __name__ =='__main__':
    numbers = [3, 8, 12, 4, 7]
    target = 11

    result = all_two_sums(numbers, target)
    print("All matching index pairs:", result)
