# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

# Example: arr = [-1,-2,-3,-4]  -> maxSum = -1 ([-1])
# arr = [1,2,3,-2,5] -> maxSum = 9  ([1,2,3,-2,5])


# Method 1: Kadane's Algorithm
def solve(arr, n):
    maxSum = -2**32
    SubarrSum = 0
    for i in range(n):
        SubarrSum += arr[i]
        maxSum = max(maxSum, SubarrSum)
        
        if SubarrSum < 0:
            SubarrSum = 0
    return maxSum

arr = [1, 5, -10, 3, 6, 9]
print(solve(arr, len(arr)))


# Method 2: Dynamic Programming
def solve(arr, n):
    maxSum = arr[0]
    SubarrSum = arr[0]
    for i in range(1, n):
        SubarrSum = max(arr[i], SubarrSum + arr[i])
        maxSum = max(maxSum, SubarrSum)

    return maxSum


# Method 3: when we've to find the subarray with max sum
def solve(arr, n):
    maxSum = -2**32
    SubarrSum = 0
    Subarr = []
    s = e = 0
    for i in range(n):
        SubarrSum += arr[i]
        if SubarrSum > maxSum:
            maxSum = SubarrSum
            e = i
            Subarr[:] = arr[s:e+1]
        
        if SubarrSum < 0:
            SubarrSum = 0
            s = i+1
    return sum(Subarr)

arr = [1, 5, -10, 3, 6, 9]
print(solve(arr, len(arr)))


# we can optimise the method 3, instead of using Subarr, we can directly find subarray
# with the help of start and end index

def solve(arr, n):
    maxSum = -2**32
    start = end = s = 0
    SubarrSum = 0
    for i in range(n):
        SubarrSum += arr[i]
        if SubarrSum > maxSum:
            maxSum = SubarrSum
            start = s
            end = i
        if SubarrSum < 0:
            SubarrSum = 0
            s = i+1
    return arr[start:end+1]

