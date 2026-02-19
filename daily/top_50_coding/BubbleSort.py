def bubbleSort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                temp= nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
    print("sorted array is ", nums)

arr =[5,7,2,8,0,1]
bubbleSort(arr)