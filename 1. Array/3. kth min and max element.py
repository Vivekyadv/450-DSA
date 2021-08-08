# find kth mininum and maximum element in array

# Method 1: sort the array, first kth element is kth minimum
# and kth element from last is kth maximum element
def solve(arr, k):
    arr.sort()
    n = len(arr)
    min_k = arr[k-1]
    max_k = arr[n-k]
    return min_k, max_k

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(solve(arr, k))