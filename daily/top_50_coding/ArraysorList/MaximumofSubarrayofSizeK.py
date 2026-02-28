def maxofSubarrayofSizeK(arr, k):
    n = (len(arr))
    window_sum = sum(arr[:k]) #   -2
    print(window_sum)
    max_sum= window_sum  #-2
    print(max_sum)
    for i in range(k, n):  #and i = 4 , k =3, n=8
        window_sum = window_sum+ arr[i] - arr[i-k]  #  3 + (-2) - (2) = -2+4+1= 3
        max_sum = max(max_sum, window_sum) # max(-2,3) = 3
    return max_sum



arr= [-1,2,-3,4,-2,1,5,-3]
k = 3
print(maxofSubarrayofSizeK(arr,k))