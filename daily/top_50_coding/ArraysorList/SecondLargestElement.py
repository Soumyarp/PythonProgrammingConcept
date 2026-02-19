def secondLargest(arr):
  largest = arr[0]
  secondLargest=float('-inf')
  for i in range(0,len(arr)):
      if arr[i]>largest:
          largest=arr[i]
  for i in range(0,len(arr)):
      if arr[i]<largest and arr[i]>secondLargest and arr[i]!=largest:
            secondLargest=arr[i]
  return secondLargest


import heapq

def kthLargest(arr, k):
    if len(arr) < k:
        return None
    return heapq.nlargest(k, set(arr))[k-1]


arr=[101,55,32,-97,2,99,3,0,45,67,101]
print(kthLargest(arr, 10))
print(secondLargest(arr))
