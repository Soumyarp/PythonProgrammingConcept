def move0sand1s(nums) -> int:
    zero_index =0
    for i in range(len(nums)):
        if nums[i] ==0:
            nums[i],nums[zero_index]= nums[zero_index], nums[i]
            zero_index+=1
    return nums
nums = [0,1,0,1,1,0]

print(move0sand1s(nums))