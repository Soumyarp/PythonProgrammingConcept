# Sliding Window - this is the technique where we need to find the max sum of a subarray for a given size K

def max_sum_subarray_k(nums,k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k,len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

nums = [2, 1, 5, 1, 3, 2]
k = 3
print("Sliding Window result:", max_sum_subarray_k(nums, k))
